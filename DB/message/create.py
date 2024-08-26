from DB.db_init import db
from fastapi import APIRouter, HTTPException
from Models.Message import Message
from datetime import datetime
from bson import ObjectId  # Import ObjectId to convert string to ObjectId
import httpx

router = APIRouter()

@router.post("/chat/{chat_id}/add-message")
async def addMessage(chat_id: str, message: Message):
    chat_entity = db.Chat
    chat_object_id = ObjectId(chat_id)
    
    # Find the chat by chat_id
    chat = chat_entity.find_one({"_id": chat_object_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Add the new message to the chat's message list
    update_result = chat_entity.update_one(
        {"_id": chat_object_id},
        {"$push": {"messages": message.dict()}}
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=500, detail="Failed to add message")
    
    # Prepare the payload for the external API request
    external_payload = {
        'chunks':chat.chunks,
        'numofresults':chat.numofresults,
        'question':message.content,
    }

    # Send the request to the other backend
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:8080/api/query/",  # Replace with the actual URL of the other backend
                json=external_payload
            )
            response.raise_for_status()  # Raises an error for 4xx/5xx responses
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Failed to notify external service")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    return {"message": "Message added successfully and external service notified"}
