# main.py
import os
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware as StarletteCORS
from starlette.applications import Starlette

from app.routes import ai_tutor, stats, sync_user, otp
from app.routes.practice import router as practice_router
from app.sockets.sio_server import sio


# ============================================================
# FASTAPI CORE APP
# ============================================================

fastapi_app = FastAPI(title="SlashCoder Backend")

FRONTEND_URL = os.getenv("FRONTEND_URL", "https://slashcoder.netlify.app")

allowed_origins = [
    FRONTEND_URL,
    "https://slashcoder.in",
    "https://www.slashcoder.in",
    "https://slashcoder.netlify.app",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# CORS for FastAPI
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
fastapi_app.include_router(ai_tutor.router)
fastapi_app.include_router(stats.router)
fastapi_app.include_router(practice_router)
fastapi_app.include_router(sync_user.router)
fastapi_app.include_router(otp.router)


@fastapi_app.get("/")
async def home():
    return {"message": "SlashCoder backend LIVE on Railway"}


@fastapi_app.get("/ping")
async def ping():
    return {"pong": True}


# ============================================================
# SOCKET.IO → wrap fastapi_app
# ============================================================

socket_app = socketio.ASGIApp(
    sio,
    other_asgi_app=fastapi_app,
    socketio_path="/socket.io"
)


# ============================================================
# FINAL ASGI APP → wrap everything with Starlette CORS
# ============================================================

application = Starlette(
    middleware=[
        Middleware(
            StarletteCORS,
            allow_origins=allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
    ]
)

# mount socket + fastapi app into starlette root
application.mount("/", socket_app)
