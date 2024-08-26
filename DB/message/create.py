from DB.db_init import db
from fastapi import APIRouter, HTTPException
from Models.Message import Message
from datetime import datetime

router = APIRouter()

@router.post("/chat/{chat_id}/add-message")
async def addMessage(chat_id: str, message: Message):
    chat_entity = db.Chat

    # Find the chat by chat_id
    chat = chat_entity.find_one({"chat_id": chat_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Add the new message to the chat's message list
    update_result = chat_entity.update_one(
        {"chat_id": chat_id},
        {"$push": {"messages": message.dict()}}
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=500, detail="Failed to add message")

    return {"message": "Message added successfully"}
