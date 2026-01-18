# app/sockets/matchmaking.py
# ======================================================
# Slashcoder Matchmaking — Clean implementation
# Features:
# - Safe matchmaking (no self-match)
# - join_queue / waiting / match_found
# - run_code (Judge0) for custom runs
# - submit_code waits for both submissions then decides winner
# - timeout rules: only-one-submitted => that player wins at timeout; none => draw
# - forfeit and disconnect handling (with reconnection window)
# - rejoin event to allow clients to re-enter a room after refresh/disconnect
# - XP rules per difficulty and draw/loss rules
# - Saves match records to Firestore and updates XP/wins/losses accordingly
# ======================================================

import random
import time
import datetime
import asyncio
import httpx
import socketio

from firebase_admin import firestore
from app.data.match_problems import PROBLEMS


# ---------- Socket.IO server (ASGI) ----------
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
    allow_credentials=True,
    logger=True,
    engineio_logger=True,
    ping_timeout=60,
    ping_interval=25,
)

# Firestore client (assumes firebase_admin.initialize_app() already run)
db = firestore.client()

# Judge0 endpoint (public CE)
JUDGE0_URL = "https://ce.judge0.com/submissions?base64_encoded=false&wait=true"
LANG_TO_ID = {"python": 71, "cpp": 54, "java": 62, "javascript": 63}

# XP configuration
XP_BY_DIFFICULTY = {
    "Very Easy": 15,
    "Easy": 20,
    "Medium": 25,
}
DRAW_XP = 10
LOSS_XP = 0  # per your request, loser gets 0 XP

# State
waiting_player = None  # dict: {sid, uid, name, xp, queued_at}
matches = {}           # room -> match dict

def gen_tests_for_problem(pid: str):
    for diff in PROBLEMS:
        for p in PROBLEMS[diff]:
            if p["id"] == pid:
                return p["tests"]
    return []


# Helpers
def normalize_text(s: str) -> str:
    if s is None: return ""
    return s.replace("\r","").strip()

def compare_output(actual: str, expected: str, case_insensitive=True) -> bool:
    a = normalize_text(actual)
    e = normalize_text(expected)
    if case_insensitive:
        return a.lower() == e.lower()
    return a == e

async def judge_run(lang: str, code: str, stdin: str):
    async with httpx.AsyncClient(timeout=30.0) as client:
        payload = {"source_code": code, "language_id": LANG_TO_ID.get(lang, 71), "stdin": stdin}
        try:
            r = await client.post(JUDGE0_URL, json=payload, headers={"Content-Type":"application/json"})
            data = r.json()
            # prefer stdout, then stderr/compile_output
            return data.get("stdout") or data.get("stderr") or data.get("compile_output") or ""
        except Exception as e:
            return f"[Judge0 error] {e}"

def get_difficulty_for_xp(xp):
    if xp < 50: return "Very Easy"
    if xp < 200: return "Easy"
    return "Medium"

def room_id_for(u1, u2):
    # deterministic room id (order independent)
    a,b = sorted([str(u1), str(u2)])
    return f"room_{a}_{b}"

# ---------- Socket event handlers ----------
@sio.event
async def connect(sid, environ):
    print("[sio] connect", sid)

@sio.event
async def disconnect(sid):
    print("[sio] disconnect", sid)
    # find match
    room = None
    for r,m in list(matches.items()):
        if sid in m.get("players", []):
            room = r
            break
    if not room:
        # if the sid was waiting in queue, remove it
        global waiting_player
        if waiting_player and waiting_player.get("sid") == sid:
            waiting_player = None
        return

    match = matches.get(room)
    if not match:
        return

    # mark disconnected and give a short reconnection window
    print(f"[disconnect] sid {sid} disconnected from {room}, waiting for reconnection")
    match.setdefault("disconnected", {})[sid] = time.time()

    # wait 10s for reconnection
    await sio.sleep(15)

    # if player reconnected, do nothing
    active_sids = set()
    mgr = getattr(sio, "manager", None)
    try:
        # engineio rooms: keep safe access
        active_sids = set(mgr.rooms.get("/", {}).keys())
    except Exception:
        pass

    if sid in active_sids:
        print("[reconnect] player returned to match:", sid)
        match.get("disconnected", {}).pop(sid, None)
        return

    # still disconnected -> opponent wins (forfeit)
    p1,p2 = match["players"]
    opponent_sid = p2 if sid == p1 else p1
    print(f"[forfeit by disconnect] {sid} did not return, opponent {opponent_sid} wins")
    await finalize_match(room, winner_sid=opponent_sid, loser_sid=sid, reason="disconnect_forfeit")


@sio.event
async def join_queue(sid, data):
    # data: { uid, name }
    global waiting_player
    uid = data.get("uid")
    name = data.get("name", "Player")

    print("[join_queue] sid", sid, "uid", uid, "name", name)

    # Ensure firestore fields exist for user
    try:
        db.collection("users").document(uid).set({
            "username": name,
            "xp": firestore.Increment(0),
            "wins": firestore.Increment(0),
            "losses": firestore.Increment(0),
            "updatedAt": datetime.datetime.utcnow()
        }, merge=True)
        snap = db.collection("users").document(uid).get()
        xp = snap.to_dict().get("xp", 0) if snap.exists() else 0
    except Exception:
        xp = 0

    # If there is a waiting player, try to match
    if waiting_player:
        # if waiting_player is same uid or same sid -> replace waiting player with new one
        if waiting_player.get("uid") == uid or waiting_player.get("sid") == sid:
            print("[queue] same user re-queued, updating waiting_player")
            waiting_player = {"sid": sid, "uid": uid, "name": name, "xp": xp, "queued_at": time.time()}
            await sio.emit("waiting", {"msg":"Waiting for opponent..."}, to=sid)
            return

        # ensure waiting player is still connected
        try:
            if not sio.manager.is_connected(waiting_player["sid"], "/"):
                print("[queue] old waiting player not connected; replacing")
                waiting_player = {"sid": sid, "uid": uid, "name": name, "xp": xp, "queued_at": time.time()}
                await sio.emit("waiting", {"msg":"Waiting for opponent..."}, to=sid)
                return
        except Exception:
            # fallback: if can't check, replace
            waiting_player = {"sid": sid, "uid": uid, "name": name, "xp": xp, "queued_at": time.time()}
            await sio.emit("waiting", {"msg":"Waiting for opponent..."}, to=sid)
            return

        # Avoid matching the player with themselves (double-click join)
        if waiting_player["uid"] == uid:
            print("[queue] self-match prevented; keeping waiting_player")
            await sio.emit("waiting", {"msg":"Waiting for opponent..."}, to=sid)
            return

        # create match
        p1 = waiting_player
        p2 = {"sid": sid, "uid": uid, "name": name, "xp": xp, "queued_at": time.time()}
        waiting_player = None

        difficulty = get_difficulty_for_xp((p1["xp"] + p2["xp"]) // 2)
        problem = random.choice(PROBLEMS[difficulty])
        tests = gen_tests_for_problem(problem["id"])


        room = room_id_for(p1["uid"], p2["uid"])
        start_time = int(time.time())

        matches[room] = {
            "players": [p1["sid"], p2["sid"]],
            "uids": [p1["uid"], p2["uid"]],
            "names": [p1["name"], p2["name"]],
            "problem": {**problem, "difficulty": difficulty},
            "tests": tests,
            "best": {},  # sid -> {passed, total, ts}
            "startTime": start_time,
            "timeLimit": 600 if difficulty == "Medium" else 300,
            "createdAt": datetime.datetime.utcnow()
        }

        # schedule timeout watcher
        asyncio.create_task(match_timeout_watch(room))

        # put both players in room and emit match_found
        await sio.enter_room(p1["sid"], room)
        await sio.enter_room(p2["sid"], room)

        payload = {
            "room": room,
            "problem": matches[room]["problem"],
            "timeLimit": matches[room]["timeLimit"],
            "testsCount": len(tests),
            "startTime": start_time
        }

        await sio.emit("match_found", {**payload, "opponent": {"name": p2["name"], "uid": p2["uid"]}}, to=p1["sid"])
        await sio.emit("match_found", {**payload, "opponent": {"name": p1["name"], "uid": p1["uid"]}}, to=p2["sid"])
        print("[match_created]", room, "players", matches[room]["names"])
        return

    # No waiting player: set this as waiting
    waiting_player = {"sid": sid, "uid": uid, "name": name, "xp": xp, "queued_at": time.time()}
    await sio.emit("waiting", {"msg":"Waiting for opponent..."}, to=sid)
    print("[queue] placed:", waiting_player)

@sio.event
async def rejoin(sid, data):
    # data: { room, uid }
    room = data.get("room")
    uid = data.get("uid")
    if not room or room not in matches:
        await sio.emit("error", {"msg":"No such match"}, to=sid)
        return
    match = matches[room]
    # find index of uid
    try:
        idx = match["uids"].index(uid)
    except ValueError:
        await sio.emit("error", {"msg":"Not part of this match"}, to=sid)
        return

    # reassign the sid into players list
    old_sid = match["players"][idx]
    match["players"][idx] = sid

    # join room
    await sio.enter_room(sid, room)
    # send match_found payload to rejoined player (do not change startTime)
    payload = {
        "room": room,
        "problem": match["problem"],
        "timeLimit": match["timeLimit"],
        "testsCount": len(match["tests"]),
        "startTime": match["startTime"]
    }
    opponent_idx = 1 - idx
    await sio.emit("match_found", {**payload, "opponent": {"name": match["names"][opponent_idx], "uid": match["uids"][opponent_idx]}}, to=sid)
    print(f"[rejoin] uid {uid} rejoined room {room} as sid {sid} (replaced {old_sid})")

@sio.event
async def run_code(sid, data):
    # data: { room, language, source_code, stdin }
    lang = data.get("language", "python")
    code = data.get("source_code", "")
    stdin = data.get("stdin", "")
    out = await judge_run(lang, code, stdin)
    await sio.emit("run_result", {"stdout": out or ""}, to=sid)

@sio.event
async def submit_code(sid, data):
    lang = data.get("language", "python")
    code = data.get("source_code", "")

    # find match for sid
    room = None
    match = None
    for r, m in matches.items():
        if sid in m.get("players", []):
            room = r
            match = m
            break

    if not room:
        await sio.emit("error", {"msg": "Not in match"}, to=sid)
        return

    # ---------------------------------------------------
    # 🔒 PREVENT MULTIPLE SUBMISSIONS
    # ---------------------------------------------------
    if "submitted" not in match:
        match["submitted"] = {}

    if match["submitted"].get(sid, False):
        return  # ignore extra clicks

    match["submitted"][sid] = True
    # ---------------------------------------------------

    passed = 0
    total = len(match["tests"])

    # run hidden tests
    for t in match["tests"]:
        stdin = t.get("input", "")
        out_raw = await judge_run(lang, code, stdin)
        out = out_raw or ""
        if compare_output(out, t.get("output", "")):
            passed += 1

    match["best"][sid] = {
        "passed": passed,
        "total": total,
        "ts": time.time()
    }

    await sio.emit("submission_result", {
        "passed": passed,
        "total": total
    }, to=sid)

    # if both submitted → decide winner
    p1, p2 = match["players"]
    if p1 in match["best"] and p2 in match["best"]:
        await sio.sleep(2)
        r1 = match["best"][p1]
        r2 = match["best"][p2]

        if r1["passed"] > r2["passed"]:
            await finalize_match(room, winner_sid=p1, loser_sid=p2, reason="more_tests_passed")
        elif r2["passed"] > r1["passed"]:
            await finalize_match(room, winner_sid=p2, loser_sid=p1, reason="more_tests_passed")
        else:
            await finalize_draw(room, reason="same_passed_tests")

            

@sio.event
async def forfeit(sid, data=None):
    # find match and mark opponent winner
    for room, match in list(matches.items()):
        if sid in match.get("players", []):
            opp = match["players"][1] if match["players"][0] == sid else match["players"][0]
            await finalize_match(room, winner_sid=opp, loser_sid=sid, reason="forfeit_button")
            break

# finalize helpers
async def finalize_match(room, winner_sid, loser_sid, reason="match_end"):
    if room not in matches:
        return
    match = matches[room]
    try:
        w_idx = match["players"].index(winner_sid)
        l_idx = match["players"].index(loser_sid)
    except ValueError:
        # cleanup if unexpected
        matches.pop(room, None)
        return

    winner_uid = match["uids"][w_idx]
    loser_uid = match["uids"][l_idx]
    problem = match["problem"]
    now = datetime.datetime.utcnow()

    # XP assignment based on difficulty (winner gets difficulty XP, loser gets LOSS_XP)
    diff = problem.get("difficulty", "Very Easy")
    win_xp = XP_BY_DIFFICULTY.get(diff, 15)

    # Update Firestore: winner + loser
    try:
        db.collection("users").document(winner_uid).set({
            "wins": firestore.Increment(1),
            "xp": firestore.Increment(win_xp),
            "updatedAt": now
        }, merge=True)
        db.collection("users").document(loser_uid).set({
            "losses": firestore.Increment(1),
            "xp": firestore.Increment(LOSS_XP),
            "updatedAt": now
        }, merge=True)
    except Exception as e:
        print("[ERROR] Firestore update:", e)

    # Save match records
    for idx, uid in enumerate(match["uids"]):
        passed = match["best"].get(match["players"][idx], {}).get("passed", 0)
        total = match["best"].get(match["players"][idx], {}).get("total", len(match["tests"]))
        try:
            db.collection("users").document(uid).collection("matches").add({
                "winnerId": winner_uid,
                "problem": problem.get("title"),
                "difficulty": problem.get("difficulty", "Unknown"),
                "passed": passed,
                "total": total,
                "endedAt": now,
                "reason": reason
            })
        except Exception as e:
            print("[ERROR] saving match:", e)

    # Emit battle_result to room
    w_name = match["names"][w_idx]
    l_name = match["names"][l_idx]
    summary = f"🏆 Winner: {w_name}"
    analytics = {
        "winner": winner_uid,
        "players": [
            {"name": w_name, "passed": match['best'].get(match['players'][w_idx], {}).get("passed", 0)},
            {"name": l_name, "passed": match['best'].get(match['players'][l_idx], {}).get("passed", 0)}
        ],
        "problem": {"title": problem.get("title"), "difficulty": problem.get("difficulty", "Unknown")},
        "reason": reason
    }

    await sio.emit("battle_result", {"summary": summary, "analytics": analytics}, room=room)

    # cleanup
    try:
        # remove players from room
        for p in match.get("players", []):
            try:
                await sio.leave_room(p, room)
            except Exception:
                pass
        del matches[room]
    except Exception:
        pass

async def finalize_draw(room, reason="draw"):
    if room not in matches:
        return
    match = matches[room]
    problem = match["problem"]
    uids = match["uids"]
    names = match["names"]
    now = datetime.datetime.utcnow()

    # Give draw XP to both
    # Give draw XP + increment draws
    try:
      for uid in uids:
            db.collection("users").document(uid).set({
                "xp": firestore.Increment(DRAW_XP),
                "draws": firestore.Increment(1),
                "updatedAt": now
            }, merge=True)
    except Exception as e:
        print("[ERROR] awarding draw xp:", e)


    # Save draw record for both
    for uid in uids:
        try:
            db.collection("users").document(uid).collection("matches").add({
                "winnerId": None,
                "problem": problem.get("title"),
                "difficulty": problem.get("difficulty", "Unknown"),
                "passed": 0,
                "total": len(match["tests"]),
                "endedAt": now,
                "result": "draw",
                "reason": reason
            })
        except Exception as e:
            print("[ERROR] saving draw:", e)

    await sio.emit("battle_result", {
        "summary": "🤝 Draw ",
        "analytics": {
            "winner": None,
            "players": [
                {"name": names[0], "passed": 0},
                {"name": names[1], "passed": 0}
            ],
            "problem": {"title": problem.get("title"), "difficulty": problem.get("difficulty")},
            "reason": reason
        }
    }, room=room)

    # cleanup
    try:
        del matches[room]
    except Exception:
        pass

# Timeout watcher
async def match_timeout_watch(room):
    # small initial sleep to ensure match object is ready
    await sio.sleep(2)
    if room not in matches:
        return
    match = matches[room]
    start_time = match.get("startTime", int(time.time()))
    time_limit = match.get("timeLimit", 300)
    now = int(time.time())
    remaining = max(0, start_time + time_limit - now)
    await sio.sleep(remaining)

    # match may already be finished
    if room not in matches:
        return
    match = matches.get(room)
    p1, p2 = match["players"]
    best = match.get("best", {})

    # CASE 1: both submitted -> nothing (submit_code handled winner)
    if p1 in best and p2 in best:
        return

    # CASE 2: only one submitted -> that player wins
    if p1 in best and p2 not in best:
        await finalize_match(room, winner_sid=p1, loser_sid=p2, reason="timeout_one_submitted")
        return
    if p2 in best and p1 not in best:
        await finalize_match(room, winner_sid=p2, loser_sid=p1, reason="timeout_one_submitted")
        return

    # CASE 3: none submitted -> draw
    await finalize_draw(room, reason="timeout_no_submissions")

# Expose ASGI app for server
import fastapi
app = fastapi.FastAPI()
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)
# mount at root in your deployment; the deployment config should use this ASGI app

# For local debug: run with `uvicorn app.sockets.matchmaking:sio_app --reload`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.sockets.matchmaking:sio_app", host="0.0.0.0", port=8000, reload=True)
