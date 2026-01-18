# app/sockets/sio_server.py

"""
SlashCoder Unified Socket.IO Server
Matchmaking + Chatrooms share the SAME Socket.IO instance
This file ONLY defines events. The global `sio` server is created in matchmaking.py
so CORS can be configured before both modules import it.
"""

import os
from app.sockets.matchmaking import sio   # Global Socket.IO instance (with CORS added in matchmaking.py)


# -------------------------------------------------------
# 🔹 Chatroom: Join Room
# -------------------------------------------------------
@sio.event
async def join_room(sid, data):
    """
    User joins a room.
    data:
    {
        "roomId": "python-room",
        "username": "Jatin"
    }
    """
    room = data.get("roomId")
    username = data.get("username", "Anonymous")

    if not room:
        print(f"[join_room] ERROR: missing roomId (sid={sid})")
        return

    await sio.enter_room(sid, room)
    print(f"[CHAT] {username} joined room {room}")

    await sio.emit(
        "system_message",
        {
            "roomId": room,
            "msg": f"{username} joined the room",
        },
        room=room,
    )


# -------------------------------------------------------
# 🔹 Chatroom: Send Message
# -------------------------------------------------------
@sio.event
async def send_message(sid, data):
    """
    Broadcast a chat message.
    data:
    {
        "roomId": "python-room",
        "text": "Hello world",
        "senderName": "Jatin"
    }
    """
    room = data.get("roomId")
    text = data.get("text")
    sender = data.get("senderName", "Anonymous")

    if not room:
        print(f"[send_message] ERROR: missing roomId (sid={sid})")
        return

    if not text:
        print(f"[send_message] ERROR: message empty (sid={sid})")
        return

    print(f"[CHAT][{room}] {sender}: {text}")

    await sio.emit(
        "receive_message",
        {
            "roomId": room,
            "text": text,
            "senderName": sender,
        },
        room=room,
    )


# -------------------------------------------------------
# 🔹 User Disconnect
# -------------------------------------------------------
@sio.event
async def disconnect(sid):
    """
    Called whenever a user's websocket closes.
    Used for matchmaking auto-forfeit.
    """
    print(f"[SOCKET] disconnected: {sid}")

    # Import here to avoid circular import
    from app.sockets.matchmaking import matches, finalize_match

    # Auto-forfeit logic
    for room, match in list(matches.items()):
        if sid in match["players"]:

            opponent = (
                match["players"][0]
                if match["players"][1] == sid
                else match["players"][1]
            )

            print(f"[MATCH] auto-forfeit: sid={sid} -> opponent wins")
            await finalize_match(room, winner_sid=opponent, loser_sid=sid)
            break
