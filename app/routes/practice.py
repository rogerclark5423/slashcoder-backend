# slashcoder-backend/app/routes/practice.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
import asyncio
import httpx

from firebase_admin import firestore
db = firestore.client()

from app.data.practice_problems import PRACTICE_PROBLEMS

router = APIRouter(prefix="/api/practice", tags=["Practice"])

# -------------------------------------------------
# 🔥 Judge0 CE (FREE, no RapidAPI required)
# -------------------------------------------------
JUDGE0_URL = "https://ce.judge0.com/submissions"

LANGUAGE_MAP = {
    "python": 71,      # Python 3
    "cpp": 54,         # C++ 17
    "c": 50,           # C (GCC)
    "java": 62,        # Java 17
    "javascript": 63   # Node.js
}

XP_MAP = {
    "Very Easy": 10,
    "Easy": 15,
    "Medium": 20
}

# -------------------------------------------------
# 🚀 MODELS
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
# 📌 GET ALL PRACTICE PROBLEMS
# -------------------------------------------------

@router.get("/problems")
async def get_problems():
    output = []

    for diff, problems in PRACTICE_PROBLEMS.items():
        for p in problems:
            output.append({
                "id": p["id"],
                "title": p["title"],
                "description": p["description"],
                "description_full": p.get("description_full", p["description"]),
                "input": p.get("input", ""),
                "output": p.get("output", ""),
                "example": p.get("example", ""),
                "constraints": p.get("constraints", ""),
                "explanation": p.get("explanation", ""),
                "difficulty": diff
            })

    return output


# -------------------------------------------------
# 🧪 Judge0 Runner
# -------------------------------------------------

async def judge_run(language: str, code: str, stdin: str):
    lang = language.lower()

    if lang not in LANGUAGE_MAP:
        raise Exception(f"Unsupported language: {language}")

    payload = {
        "language_id": LANGUAGE_MAP[lang],
        "source_code": code,
        "stdin": stdin
    }

    async with httpx.AsyncClient() as client:

        # 1️⃣ Create submission
        res = await client.post(f"{JUDGE0_URL}?wait=false", json=payload)
        token = res.json().get("token")

        if not token:
            raise Exception("Failed to get Judge0 token")

        # 2️⃣ Poll for result
        for _ in range(50):
            await asyncio.sleep(0.20)
            status = await client.get(f"{JUDGE0_URL}/{token}")
            data = status.json()

            if data.get("status", {}).get("id") not in [1, 2]:
                break

        stdout = data.get("stdout") or ""
        stderr = data.get("stderr") or ""
        compile_err = data.get("compile_output") or ""

        if compile_err:
            return f"[Compile Error]\n{compile_err}"

        if stderr:
            return f"[Runtime Error]\n{stderr}"

        return stdout


# -------------------------------------------------
# ▶ RUN CODE (custom input)
# -------------------------------------------------

@router.post("/run")
async def run_code(payload: RunPayload):
    try:
        result = await judge_run(
            payload.language,
            payload.code,
            payload.stdin or ""
        )

        return {
            "mode": "custom",
            "stdout": result or ""
        }

    except Exception as e:
        return {
            "mode": "custom",
            "error": str(e)
        }


# -------------------------------------------------
# 🧩 HIDDEN TEST RUN
# -------------------------------------------------

def compare_output(got: str, expected: str) -> bool:
    return got.strip() == expected.strip()


@router.post("/submit")
async def submit_code(payload: SubmitPayload):

    # 1️⃣ Find problem
    problem = None
    difficulty = None

    for diff, arr in PRACTICE_PROBLEMS.items():
        for p in arr:
            if p["id"] == payload.pid:
                problem = p
                difficulty = diff
                break
        if problem:
            break

    if not problem:
        raise HTTPException(404, "Problem not found")

    tests = problem.get("tests", [])

    if not tests:
        raise HTTPException(400, "No testcases available")

    # 2️⃣ Run hidden tests
    passed = 0
    results = []

    for i, t in enumerate(tests):
        test_input = t.get("input", "")
        expected = str(t.get("output", "")).strip()

        try:
            raw = await judge_run(payload.language, payload.code, test_input)
            got = (raw or "").strip()
        except Exception as e:
            got = f"[error] {e}"

        ok = compare_output(got, expected)
        if ok:
            passed += 1

        results.append({
            "index": i + 1,
            "input": test_input,
            "expected": expected,
            "got": got,
            "passed": ok
        })

    total = len(tests)
    completed = passed == total

    # 3️⃣ XP update
    xp_gain = 0

    if completed:
        xp_gain = XP_MAP.get(difficulty, 10)

        db.collection("users").document(payload.uid).set({
            "xp": firestore.Increment(xp_gain),
            "practiceCompleted": firestore.ArrayUnion([payload.pid]),
            "updatedAt": datetime.datetime.utcnow()
        }, merge=True)

    return {
        "passed": passed,
        "total": total,
        "xp_gain": xp_gain,
        "completed": completed,
        "results": results
    }
