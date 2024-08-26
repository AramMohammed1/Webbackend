from DB.db_init import db
from fastapi import APIRouter, HTTPException
from bson import ObjectId  # Import ObjectId to convert string to ObjectId

router = APIRouter()

@router.get("/chat/{chat_id}")
async def getChat(chat_id: str):
    chat_entity = db.Chat
    try:
        chat_object_id = ObjectId(chat_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid chat ID format")
    chat = chat_entity.find_one({"_id": chat_object_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    chat['_id'] = str(chat['_id'])
    # Return the chat data
    return chat

