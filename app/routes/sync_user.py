# slashcoder-backend/app/routes/sync_user.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.firebase_init import db
from datetime import datetime

router = APIRouter(prefix="/api", tags=["User Sync"])

# -----------------------
# Payload Model
# -----------------------
class SyncPayload(BaseModel):
    uid: str
    email: str
    displayName: str | None = None
    photoURL: str | None = None


# -----------------------
# User Sync Route
# -----------------------
@router.post("/sync-user")
async def sync_user(payload: SyncPayload):

    uid = payload.uid

    # Reference to Firestore user doc
    user_ref = db.collection("users").document(uid)

    # Check if user exists
    snapshot = user_ref.get()

    if snapshot.exists:
        # UPDATE EXISTING USER
        data = snapshot.to_dict()

        updated_data = {
            "email": payload.email,
            "displayName": payload.displayName or data.get("displayName"),
            "photoURL": payload.photoURL or data.get("photoURL"),
            "updatedAt": datetime.utcnow().isoformat(),
        }

        user_ref.update(updated_data)

        return {
            "status": "updated",
            "profile": {**data, **updated_data}
        }

    else:
        # CREATE NEW USER
        new_user = {
            "uid": uid,
            "email": payload.email,
            "displayName": payload.displayName or "New User",
            "photoURL": payload.photoURL or None,
            "xp": 0,
            "level": 1,
            "coins": 0,
            "solvedCount": 0,
            "joinedAt": datetime.utcnow().isoformat(),
            "updatedAt": datetime.utcnow().isoformat(),
        }

        user_ref.set(new_user)

        return {
            "status": "created",
            "profile": new_user
        }
