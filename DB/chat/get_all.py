from backend.DB.db_init import db
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/user/{user_email}/chats")
async def getAllChatsForUser(user_email: str):
    chat_entity = db.Chat

    # Find all chats where the user is a participant
    user_chats = list(chat_entity.find({"participants": user_email}))
    
    if not user_chats:
        raise HTTPException(status_code=404, detail="No chats found for this user")
  
    # Return the list of chats
    return user_chats
