from backend.DB.db_init import db
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/chat/{chat_id}")
async def getChat(chat_id: str):
    chat_entity = db.Chat

    # Find the chat by chat_id
    chat = chat_entity.find_one({"chat_id": chat_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Return the chat data
    return chat

