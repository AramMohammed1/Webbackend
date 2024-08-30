from externals.DB.db_init import db
from fastapi import APIRouter, HTTPException
from core.models.Chat import Chat

router = APIRouter()

@router.post("/chat/delete")
async def deleteChat(chat_id: str):
    chat_entity = db.Chat

    # Attempt to delete the chat by chat_id
    delete_result = chat_entity.delete_one({"chat_id": chat_id})

    # Check if the chat was found and deleted
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Chat not found")

    return {"message": "Chat deleted successfully"}
