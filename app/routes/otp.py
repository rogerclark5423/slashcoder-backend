from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.firebase_init import db
from datetime import datetime, timedelta
import random
import os

# Brevo API SDK
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


router = APIRouter(prefix="/otp", tags=["OTP Verification"])


class OTPRequest(BaseModel):
    email: str


class OTPVerify(BaseModel):
    email: str
    code: str


# ======================================================
# EMAIL SENDER — Using Brevo EMAIL API (RECOMMENDED)
# ======================================================
def send_email(to_email, otp):
    api_key = os.getenv("BREVO_API_KEY")

    if not api_key:
        raise HTTPException(500, "Brevo API key missing on server.")

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    subject = "SlashCoder Verification Code"

    html_content = f"""
        <div style="font-family:Arial; font-size:16px;">
            <p>Your <b>SlashCoder</b> verification code is:</p>
            <h2 style="color:#ff4757;">{otp}</h2>
            <p>This OTP is valid for <b>5 minutes</b>.</p>
        </div>
    """

    email_payload = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        sender={"email": "no-reply@slashcoder.in", "name": "SlashCoder"},
        subject=subject,
        html_content=html_content,
    )

    try:
        api_instance.send_transac_email(email_payload)
    except ApiException as e:
        print("BREVO API ERROR:", e)
        raise HTTPException(500, "Failed to send OTP email.")


# ======================================================
# SEND OTP
# ======================================================
@router.post("/send")
async def send_otp(payload: OTPRequest):
    email = payload.email.strip().lower()

    otp_ref = db.collection("otps").document(email)
    log_ref = db.collection("otp_logs").document(email)

    now = datetime.utcnow()

    # Rate limit logs
    log_snap = log_ref.get()

    if log_snap.exists:
        data = log_snap.to_dict()
        timestamps = data.get("timestamps", [])

        # keep last 1 hour logs
        timestamps = [
            ts for ts in timestamps
            if datetime.fromisoformat(ts) > now - timedelta(hours=1)
        ]

        if len(timestamps) >= 5:
            raise HTTPException(429, "Too many OTP requests. Try again later.")

        timestamps.append(now.isoformat())
        log_ref.set({"timestamps": timestamps})
    else:
        log_ref.set({"timestamps": [now.isoformat()]})

    # Generate OTP
    otp = str(random.randint(100000, 999999))
    expires = now + timedelta(minutes=5)

    otp_ref.set({
        "code": otp,
        "expiresAt": expires.isoformat(),
    })

    # Send email using Brevo API
    send_email(email, otp)

    return {"message": "OTP sent successfully"}


# ======================================================
# VERIFY OTP
# ======================================================
@router.post("/verify")
async def verify_otp(payload: OTPVerify):
    email = payload.email.strip().lower()
    code = payload.code.strip()

    snap = db.collection("otps").document(email).get()

    if not snap.exists:
        raise HTTPException(400, "OTP not found or expired")

    data = snap.to_dict()

    if data["code"] != code:
        raise HTTPException(400, "Incorrect OTP")

    if datetime.utcnow() > datetime.fromisoformat(data["expiresAt"]):
        db.collection("otps").document(email).delete()
        raise HTTPException(400, "OTP expired")

    db.collection("otps").document(email).delete()

    return {"verified": True}
