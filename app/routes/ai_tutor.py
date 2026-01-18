# app/routes/ai_tutor.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
from openai import OpenAI
import os

router = APIRouter(prefix="/ai", tags=["Slash AI"])

# ---------------------------------------
# 🔐 LOAD OPENAI KEY
# ---------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=OPENAI_API_KEY)

MODEL = "gpt-4.1-mini"     # ⭐ ChatGPT model


# =================================================
# 🟩 NORMAL (NON-STREAMING) RESPONSE
# =================================================
@router.post("/tutor")
async def ai_tutor(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "").strip()

    if not prompt:
        return {"response": "⚠️ Empty prompt."}

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
        )

        msg = completion.choices[0].message
        text = msg.get("content") if isinstance(msg, dict) else msg.content

        return {"response": text or "⚠️ ChatGPT returned no text."}

    except Exception as e:
        return JSONResponse({"response": f"⚠️ Error: {str(e)}"}, status_code=500)


# =================================================
# ⚡ STREAMING RESPONSE
# =================================================
@router.post("/tutor/stream")
async def ai_tutor_stream(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "").strip()

    if not prompt:
        return StreamingResponse(iter(["⚠️ Empty prompt"]), media_type="text/plain")

    def generate_stream():
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800,
                stream=True,
            )

            for chunk in stream:
                choice = chunk.choices[0]
                delta = choice.delta

                # SDK Safety: delta may be dict or object
                content = (
                    delta.get("content")
                    if isinstance(delta, dict)
                    else getattr(delta, "content", None)
                )

                if content:
                    yield content

        except Exception as e:
            yield f"[Error] {str(e)}"

    return StreamingResponse(generate_stream(), media_type="text/plain")
