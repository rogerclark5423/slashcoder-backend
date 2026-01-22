# app/sockets/matchmaking.py
import random
import time
import datetime
import asyncio
import httpx
import socketio
import logging

from firebase_admin import firestore
from app.data.match_problems import PROBLEMS

logger = logging.getLogger("matchmaking")
logger.setLevel(logging.INFO)

# ---------- Socket.IO server (ASGI) ----------
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
    allow_credentials=True,
    logger=False,
    engineio_logger=False,
    ping_timeout=60,
    ping_interval=25,
)

# Firestore client (assumes firebase_admin.initialize_app() already run)
db = firestore.client()

# Judge0 endpoint (public CE)
JUDGE0_URL = "https://ce.judge0.com/submissions?base64_encoded=false&wait=true"
LANG_TO_ID = {"python": 71, "cpp": 54, "java": 62, "javascript": 63, "c": 50}



# XP configuration
XP_BY_DIFFICULTY = {
    "Very Easy": 15,
    "Easy": 20,
    "Medium": 25,
}
DRAW_XP = 10
LOSS_XP = 0  # per your request, loser gets 0 XP

# State
waiting_player = None  # dict: {sid, uid, username, xp, queued_at}
matches = {}           # room -> match dict

WAITING_PLAYER_TTL = 60  # seconds

def is_waiting_player_valid(waiting_player):
    if not waiting_player:
        return False

    # expired
    if time.time() - waiting_player.get("queued_at", 0) > WAITING_PLAYER_TTL:
        return False

    # still connected
    try:
        return sio.manager.is_connected(waiting_player["sid"], "/")
    except Exception:
        return False




def gen_tests_for_problem(pid: str):
    for diff in PROBLEMS:
        for p in PROBLEMS[diff]:
            if p["id"] == pid:
                return p.get("tests", [])
    return []


# Helpers
def normalize_text(s: str) -> str:
    if s is None:
        return ""
    return s.replace("\r", "").strip()


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
            r = await client.post(JUDGE0_URL, json=payload, headers={"Content-Type": "application/json"})
            data = r.json()
            # Judge0 returns: stdout, stderr, compile_output
            return {"stdout": data.get("stdout") or "", "stderr": data.get("stderr") or data.get("compile_output") or ""}
        except Exception as e:
            return {"stdout": "", "stderr": f"[Judge0 error] {e}"}


def get_difficulty_for_xp(xp):
    if xp < 50:
        return "Very Easy"
    if xp < 200:
        return "Easy"
    return "Medium"


def room_id_for(u1, u2):
    # deterministic room id (order independent)
    a, b = sorted([str(u1), str(u2)])
    return f"room_{a}_{b}"

def safe_language(lang: str) -> str:
    """
    Allow only supported languages.
    Fallback to python if invalid language is sent.
    """
    return lang if lang in LANG_TO_ID else "python"



# ---------- Socket event handlers ----------
@sio.event
async def connect(sid, environ):
    logger.info("[sio] connect %s", sid)


@sio.event
async def disconnect(sid):
    logger.info("[sio] disconnect %s", sid)
    # find match
    room = None
    for r, m in list(matches.items()):
        if sid in m.get("players", []):
            room = r
            break
    if not room:
        # if the sid was waiting in queue, remove it
        global waiting_player
        if waiting_player and waiting_player.get("sid") == sid:
            waiting_player = None
            logger.info("[queue] waiting player disconnected, cleared")

        return

    match = matches.get(room)
    if not match:
        return

    # mark disconnected and give a short reconnection window
    logger.info("[disconnect] sid %s disconnected from %s — waiting for reconnection", sid, room)
    match.setdefault("disconnected", {})[sid] = time.time()

    # wait 15s for reconnection
    await sio.sleep(15)

    # check if player reconnected (safe access)
    active_sids = set()
    mgr = getattr(sio, "manager", None)
    try:
        active_sids = set(mgr.rooms.get("/", {}).keys())
    except Exception:
        pass

    if sid in active_sids:
        logger.info("[reconnect] player returned to match: %s", sid)
        match.get("disconnected", {}).pop(sid, None)
        return

    # still disconnected -> opponent wins (forfeit)
    try:
        p1, p2 = match["players"]
    except Exception:
        matches.pop(room, None)
        return

    opponent_sid = p2 if sid == p1 else p1
    logger.info("[forfeit by disconnect] %s did not return, opponent %s wins", sid, opponent_sid)
    await finalize_match(room, winner_sid=opponent_sid, loser_sid=sid, reason="disconnect_forfeit")

@sio.event
async def leave_queue(sid, data):
    global waiting_player

    if waiting_player and waiting_player.get("sid") == sid:
        waiting_player = None
        logger.info("[queue] player left queue manually")



@sio.event
async def join_queue(sid, data):
    global waiting_player

    uid = data.get("uid")
    username = data.get("name") or data.get("username") or "Player"

    # 1️⃣ BASIC VALIDATION
    if not uid:
        await sio.emit("error", {"msg": "Missing uid"}, to=sid)
        return

    # 2️⃣ ENSURE USER EXISTS + FETCH XP
    try:
        db.collection("users").document(uid).set(
            {
                "username": username,
                "xp": firestore.Increment(0),
                "wins": firestore.Increment(0),
                "losses": firestore.Increment(0),
                "updatedAt": datetime.datetime.utcnow(),
            },
            merge=True,
        )
        snap = db.collection("users").document(uid).get()
        xp = snap.to_dict().get("xp", 0) if snap.exists() else 0
    except Exception:
        xp = 0

    # 3️⃣ CLEAN INVALID WAITING PLAYER
    if waiting_player and not is_waiting_player_valid(waiting_player):
        waiting_player = None

    # prevent same user from joining twice
    if waiting_player and waiting_player.get("uid") == uid:
        await sio.emit("waiting", {"msg": "Already in queue..."}, to=sid)
        return


    # 4️⃣ MATCH OR QUEUE
    if waiting_player:
        # prevent self-match
        if waiting_player["uid"] == uid:
            waiting_player = {
                "sid": sid,
                "uid": uid,
                "username": username,
                "xp": xp,
                "queued_at": time.time(),
            }
            await sio.emit("waiting", {"msg": "Waiting for opponent..."}, to=sid)
            return

        p1 = waiting_player
        p2 = {
            "sid": sid,
            "uid": uid,
            "username": username,
            "xp": xp,
            "queued_at": time.time(),
        }

        waiting_player = None  # 🔒 CRITICAL

        difficulty = get_difficulty_for_xp((p1["xp"] + p2["xp"]) // 2)
        problem = random.choice(PROBLEMS[difficulty])
        tests = gen_tests_for_problem(problem["id"])

        room = room_id_for(p1["uid"], p2["uid"])
        start_time = int(time.time())

        matches[room] = {
            "players": [p1["sid"], p2["sid"]],
            "uids": [p1["uid"], p2["uid"]],
            "usernames": [p1["username"], p2["username"]],
            "names": [p1["username"], p2["username"]],
            "problem": {**problem, "difficulty": difficulty},
            "tests": tests,
            "best": {},
            "submitted": {},
            "startTime": start_time,
            "timeLimit": 600 if difficulty == "Medium" else 300,
            "createdAt": datetime.datetime.utcnow(),
        }

        asyncio.create_task(match_timeout_watch(room))

        await sio.enter_room(p1["sid"], room)
        await sio.enter_room(p2["sid"], room)

        payload = {
            "room": room,
            "problem": matches[room]["problem"],
            "timeLimit": matches[room]["timeLimit"],
            "testsCount": len(tests),
            "startTime": start_time,
        }

        await sio.emit(
            "match_found",
            {**payload, "opponent": {"username": p2["username"], "uid": p2["uid"]}},
            to=p1["sid"],
        )
        await sio.emit(
            "match_found",
            {**payload, "opponent": {"username": p1["username"], "uid": p1["uid"]}},
            to=p2["sid"],
        )

        logger.info("[match_created] %s players %s", room, matches[room]["names"])
        return

    # 5️⃣ NO ONE WAITING → QUEUE
    waiting_player = {
        "sid": sid,
        "uid": uid,
        "username": username,
        "xp": xp,
        "queued_at": time.time(),
    }
    await sio.emit("waiting", {"msg": "Waiting for opponent..."}, to=sid)
    logger.info("[queue] placed: %s", waiting_player)

@sio.event
async def match_message(sid, data):
    """
    data: { room, sender, text, time }
    Broadcast chat messages inside match room.
    """
    room = data.get("room")
    text = data.get("text")
    sender = data.get("sender")

    if not room or room not in matches or not text:
        return

    await sio.emit(
        "match_message",
        {
            "sender": sender,
            "text": text,
            "time": data.get("time"),
        },
        room=room,
    )

@sio.event
async def rejoin(sid, data):
    """
    data: { room, uid }
    Reassigns the sid for a user (useful after refresh). Emits match_found back to client to restore UI.
    """
    room = data.get("room")
    uid = data.get("uid")
    if not room or room not in matches:
        await sio.emit("error", {"msg": "No such match"}, to=sid)
        return
    match = matches[room]
    try:
        idx = match["uids"].index(uid)
    except ValueError:
        await sio.emit("error", {"msg": "Not part of this match"}, to=sid)
        return

    old_sid = match["players"][idx]
    match["players"][idx] = sid

    # remove any prior disconnected record for this sid
    match.get("disconnected", {}).pop(old_sid, None)
    match.get("disconnected", {}).pop(sid, None)

    # join room
    await sio.enter_room(sid, room)
    payload = {
        "room": room,
        "problem": match["problem"],
        "timeLimit": match["timeLimit"],
        "testsCount": len(match["tests"]),
        "startTime": match["startTime"],
    }
    opponent_idx = 1 - idx
    await sio.emit(
        "match_found",
        {**payload, "opponent": {"username": match["usernames"][opponent_idx], "uid": match["uids"][opponent_idx]}},
        to=sid,
    )
    logger.info("[rejoin] uid %s rejoined room %s as sid %s (replaced %s)", uid, room, sid, old_sid)


@sio.event
async def run_code(sid, data):
    """
    data: { room(optional), uid(optional), language, source_code, stdin }
    Returns run_result -> { stdout, stderr }
    """
    lang = safe_language(data.get("language", "python"))
    code = data.get("source_code", "") or ""
    stdin = data.get("stdin", "") or ""

    # Optional: if room+uid provided and sid not currently associated, try to rebind
    room = data.get("room")
    uid = data.get("uid")
    if room and uid and room in matches:
        match = matches[room]
        # attempt to bind uid -> sid (in case client refreshed)
        try:
            idx = match["uids"].index(uid)
            if match["players"][idx] != sid:
                logger.info(
                    "[run_code] rebind sid for uid %s in room %s (old sid %s -> new sid %s)",
                    uid,
                    room,
                    match["players"][idx],
                    sid,
                )
                match["players"][idx] = sid
        except ValueError:
            pass

    out = await judge_run(lang, code, stdin)
    await sio.emit("run_result", {"stdout": out.get("stdout", ""), "stderr": out.get("stderr", "")}, to=sid)


@sio.event
async def submit_code(sid, data):
    """
    data: { room(optional), uid(optional), language, source_code }
    Behavior:
      - If room + uid provided, will try to map uid->sid (helpful after refresh).
      - Runs all tests server-side and emits submission_result to submitter with details.
      - If both players have submitted, decides winner/draw.
    """
    lang = safe_language(data.get("language", "python"))
    code = data.get("source_code", "") or ""
    room = data.get("room")
    uid = data.get("uid")

    # find match for sid OR use provided room+uid
    match = None
    if room and room in matches:
        match = matches[room]
        # if uid provided, ensure sid is in players (rebind if necessary)
        if uid:
            try:
                idx = match["uids"].index(uid)
                if match["players"][idx] != sid:
                    logger.info(
                        "[submit_code] rebind sid for uid %s in room %s (old %s -> new %s)",
                        uid,
                        room,
                        match["players"][idx],
                        sid,
                    )
                    match["players"][idx] = sid
            except ValueError:
                # uid not part of this match
                pass
    else:
        # fallback: find by sid
        for r, m in matches.items():
            if sid in m.get("players", []):
                room = r
                match = m
                break

    if not room or not match:
        await sio.emit("error", {"msg": "Not in match"}, to=sid)
        return

    # Ensure submitted dict exists
    match.setdefault("submitted", {})

    # prevent multiple submissions by same sid
    if match["submitted"].get(sid, False):
        # ignore duplicates silently
        return
    match["submitted"][sid] = True

    # Run tests (respecting per-test visibility)
    tests = match.get("tests", [])
    total = len(tests)
    passed = 0
    details = []
    for idx, t in enumerate(tests, start=1):
        stdin = t.get("input", "")
        out_raw = await judge_run(lang, code, stdin)
        out = (out_raw.get("stdout", "") or "").strip()
        expected = t.get("output", "")
        ok = compare_output(out, expected)
        if ok:
            passed += 1

        # decide visibility for this test (default: hidden)
        is_hidden = bool(t.get("hidden", True))

        detail = {
            "index": idx,
            "passed": ok,
            "input": t.get("input", ""),
            "hidden": is_hidden,
        }

        # Only include expected/actual for non-hidden tests (frontend will show them)
        if not is_hidden:
            detail["expected"] = expected
            detail["actual"] = out

        details.append(detail)

    # store best result for this sid
    match.setdefault("best", {})
    match["best"][sid] = {"passed": passed, "total": total, "ts": time.time()}

    # emit submission_result (to submitter) including details array (hidden tests flagged)
    try:
        await sio.emit("submission_result", {"passed": passed, "total": total, "details": details}, to=sid)
    except Exception:
        logger.exception("emit submission_result failed for sid %s", sid)

    # if both submitted -> decide winner
    try:
        p1, p2 = match["players"]
    except Exception:
        # malformed match -> cleanup
        matches.pop(room, None)
        return

    if p1 in match.get("best", {}) and p2 in match.get("best", {}):
        await sio.sleep(1.0)  # short pause for UI
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
    # data may contain room/uid, but fallback to sid search
    room = None
    match = None
    if data:
        room = data.get("room")
        uid = data.get("uid")
        if room and room in matches:
            match = matches[room]
            # attempt to locate sid by uid
            if uid:
                try:
                    idx = match["uids"].index(uid)
                    sid_from_match = match["players"][idx]
                    sid = sid_from_match
                except Exception:
                    pass

    if not match:
        # search by sid
        for r, m in list(matches.items()):
            if sid in m.get("players", []):
                room = r
                match = m
                break

    if not match:
        return

    opp = match["players"][1] if match["players"][0] == sid else match["players"][0]
    await finalize_match(room, winner_sid=opp, loser_sid=sid, reason="forfeit_button")


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

    # XP assignment
    diff = problem.get("difficulty", "Very Easy")
    win_xp = XP_BY_DIFFICULTY.get(diff, 15)

    # Update Firestore: winner + loser
    try:
        db.collection("users").document(winner_uid).set(
            {"wins": firestore.Increment(1), "xp": firestore.Increment(win_xp), "updatedAt": now}, merge=True
        )
        db.collection("users").document(loser_uid).set(
            {"losses": firestore.Increment(1), "xp": firestore.Increment(LOSS_XP), "updatedAt": now}, merge=True
        )
    except Exception as e:
        logger.exception("Firestore update failed: %s", e)

    # Save match records per user
    for idx, uid in enumerate(match["uids"]):
        passed = match.get("best", {}).get(match["players"][idx], {}).get("passed", 0)
        total = match.get("best", {}).get(match["players"][idx], {}).get("total", len(match["tests"]))
        try:
            db.collection("users").document(uid).collection("matches").add(
                {
                    "winnerId": winner_uid,
                    "problem": problem.get("title"),
                    "difficulty": problem.get("difficulty", "Unknown"),
                    "passed": passed,
                    "total": total,
                    "endedAt": now,
                    "reason": reason,
                }
            )
        except Exception:
            logger.exception("saving match record failed for uid %s", uid)

    # Emit battle_result to room (includes summary + analytics)
    w_name = match.get("names", [None, None])[w_idx] if match.get("names") else match.get("usernames", [None, None])[w_idx]
    l_name = match.get("names", [None, None])[l_idx] if match.get("names") else match.get("usernames", [None, None])[l_idx]
    summary = f"🏆 Winner: {w_name}"
    analytics = {
        "winner": winner_uid,
        "players": [
            {"name": w_name, "passed": match.get("best", {}).get(match["players"][w_idx], {}).get("passed", 0)},
            {"name": l_name, "passed": match.get("best", {}).get(match["players"][l_idx], {}).get("passed", 0)},
        ],
        "problem": {"title": problem.get("title"), "difficulty": problem.get("difficulty", "Unknown")},
        "reason": reason,
    }

    await sio.emit("battle_result", {"summary": summary, "analytics": analytics}, room=room)

    # cleanup
    try:
        for p in match.get("players", []):
            try:
                await sio.leave_room(p, room)
            except Exception:
                pass
        del matches[room]
    except Exception:
        logger.exception("Error during cleanup for room %s", room)


async def finalize_draw(room, reason="draw"):
    if room not in matches:
        return
    match = matches[room]
    problem = match["problem"]
    uids = match["uids"]
    names = match.get("names") or match.get("usernames") or [None, None]
    now = datetime.datetime.utcnow()

    # Give draw XP to both and increment draws
    try:
        for uid in uids:
            db.collection("users").document(uid).set(
                {"xp": firestore.Increment(DRAW_XP), "draws": firestore.Increment(1), "updatedAt": now}, merge=True
            )
    except Exception:
        logger.exception("awarding draw xp failed")

    # Save draw record for both
    for uid in uids:
        try:
            db.collection("users").document(uid).collection("matches").add(
                {
                    "winnerId": None,
                    "problem": problem.get("title"),
                    "difficulty": problem.get("difficulty", "Unknown"),
                    "passed": 0,
                    "total": len(match.get("tests", [])),
                    "endedAt": now,
                    "result": "draw",
                    "reason": reason,
                }
            )
        except Exception:
            logger.exception("saving draw record failed for uid %s", uid)

    await sio.emit(
        "battle_result",
        {
            "summary": "🤝 Draw",
            "analytics": {
                "winner": None,
                "players": [
                    {
                        "name": names[0],
                        "passed": match.get("best", {}).get(match.get("players", [None, None])[0], {}).get("passed", 0),
                    },
                    {
                        "name": names[1],
                        "passed": match.get("best", {}).get(match.get("players", [None, None])[1], {}).get("passed", 0),
                    },
                ],
                "problem": {"title": problem.get("title"), "difficulty": problem.get("difficulty")},
                "reason": reason,
            },
        },
        room=room,
    )

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
    if remaining > 0:
        await sio.sleep(remaining)

    # match may already be finished
    if room not in matches:
        return
    match = matches.get(room)
    try:
        p1, p2 = match["players"]
    except Exception:
        # nothing to do
        matches.pop(room, None)
        return
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

# For local debug: run with `uvicorn app.sockets.matchmaking:sio_app --reload`
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.sockets.matchmaking:sio_app", host="0.0.0.0", port=8000, reload=True)
