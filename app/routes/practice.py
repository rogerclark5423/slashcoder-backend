from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
import asyncio
import httpx

# -------------------------------------------------
# 🔥 FIREBASE SAFE INIT
# -------------------------------------------------
import firebase_admin
from firebase_admin import firestore

if not firebase_admin._apps:
    firebase_admin.initialize_app()

db = firestore.client()

# -------------------------------------------------
# DATA
# -------------------------------------------------
from app.data.practice_problems import PRACTICE_PROBLEMS

router = APIRouter(prefix="/api/practice", tags=["Practice"])

# -------------------------------------------------
# 🔥 Judge0
# -------------------------------------------------
JUDGE0_URL = "https://ce.judge0.com/submissions"

LANGUAGE_MAP = {
    "python": 71,
    "cpp": 54,
    "c": 50,
    "java": 62,
    "javascript": 63,
}

XP_MAP = {
    "Very Easy": 10,
    "Easy": 15,
    "Medium": 20,
}

# -------------------------------------------------
# MODELS
# -------------------------------------------------
class RunPayload(BaseModel):
    language: str
    code: str
    stdin: str = ""


class SubmitPayload(BaseModel):
    uid: str
    pid: str
    language: str
    code: str


# -------------------------------------------------
# 📌 GET PRACTICE PROBLEMS (🔥 FIXED)
# -------------------------------------------------
@router.get("/problems")
async def get_problems():
    output = []

    for difficulty, topics in PRACTICE_PROBLEMS.items():
        for topic, problems in topics.items():
            for p in problems:
                output.append({
                    "id": p["id"],
                    "title": p["title"],
                    "topic": topic,
                    "description": p.get("description", ""),
                    "description_full": p.get("description_full", ""),
                    "input": p.get("input", ""),
                    "output": p.get("output", ""),
                    "example": p.get("example", ""),
                    "constraints": p.get("constraints", ""),
                    "explanation": p.get("explanation", ""),
                    "difficulty": difficulty
                })

    return output


# -------------------------------------------------
# 🧪 Judge0 Runner
# -------------------------------------------------
async def judge_run(language: str, code: str, stdin: str):
    lang = language.lower()
    if lang not in LANGUAGE_MAP:
        raise Exception("Unsupported language")

    payload = {
        "language_id": LANGUAGE_MAP[lang],
        "source_code": code,
        "stdin": stdin
    }

    async with httpx.AsyncClient(timeout=20) as client:
        res = await client.post(f"{JUDGE0_URL}?wait=false", json=payload)
        token = res.json().get("token")
        if not token:
            raise Exception("Judge0 error")

        for _ in range(40):
            await asyncio.sleep(0.25)
            r = await client.get(f"{JUDGE0_URL}/{token}")
            data = r.json()
            if data.get("status", {}).get("id") not in [1, 2]:
                break

        if data.get("compile_output"):
            return data["compile_output"]
        if data.get("stderr"):
            return data["stderr"]

        return (data.get("stdout") or "").strip()


# -------------------------------------------------
# ▶ RUN
# -------------------------------------------------
@router.post("/run")
async def run_code(payload: RunPayload):
    try:
        out = await judge_run(payload.language, payload.code, payload.stdin)
        return {"stdout": out}
    except Exception as e:
        return {"error": str(e)}


# -------------------------------------------------
# 🧩 SUBMIT
# -------------------------------------------------
@router.post("/submit")
async def submit_code(payload: SubmitPayload):

    problem = None
    difficulty = None

    for diff, topics in PRACTICE_PROBLEMS.items():
        for _, arr in topics.items():
            for p in arr:
                if p["id"] == payload.pid:
                    problem = p
                    difficulty = diff
                    break

    if not problem:
        raise HTTPException(404, "Problem not found")

    tests = problem.get("tests", [])
    passed = 0
    results = []

    for i, t in enumerate(tests):
        expected = str(t["output"]).strip()
        got = await judge_run(payload.language, payload.code, t["input"])
        ok = got.strip() == expected

        if ok:
            passed += 1

        results.append({
            "index": i + 1,
            "passed": ok,
            "expected": expected,
            "got": got
        })

    completed = passed == len(tests)
    xp = XP_MAP.get(difficulty, 10) if completed else 0

    if completed:
        db.collection("users").document(payload.uid).set({
            "xp": firestore.Increment(xp),
            "practiceCompleted": firestore.ArrayUnion([payload.pid]),
            "updatedAt": datetime.datetime.utcnow()
        }, merge=True)

    return {
        "passed": passed,
        "total": len(tests),
        "completed": completed,
        "xp_gain": xp,
        "results": results
    }
