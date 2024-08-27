from fastapi import APIRouter, HTTPException
from DB.db_init import db
from bson import ObjectId

router = APIRouter()

def chat_serializer(chat):
    return {
        "_id": str(chat['_id']),
        "title": chat.get('title', 'Untitled'),  # Use a default value like "Untitled" if "title" is missing
        # Add other fields you want to return here
    }

@router.get("/user/{user_email}/chats")
async def getAllChatsForUser(user_email: str):
    chat_entity = db.Chat

    # Find all chats where the user is a participant
    user_chats = list(chat_entity.find({"participants": user_email}))

    if not user_chats:
        raise HTTPException(status_code=404, detail="No chats found for this user")

    # Convert each chat to a serializable format
    serialized_chats = [chat_serializer(chat) for chat in user_chats]

    return {"chats":serialized_chats}
