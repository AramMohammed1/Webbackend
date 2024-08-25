from DB.db_init import db
from fastapi import APIRouter, HTTPException
from Models.Chat import Chat
from Models.Message import Message
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()

@router.post("/chat/add")
async def addChat(
   chat:Chat
):
    chat_entity = db.Chat


    # Insert the new chat into the database
    chat_entity.insert_one({"participants":chat.participants,
                          
                            })

    return {"message": "Chat added successfully"}
