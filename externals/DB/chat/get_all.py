from fastapi import  HTTPException
from externals.DB.db_init import db

def chat_serializer(chat):
    return {
        "_id": str(chat['_id']),
        "title": chat.get('title', 'Untitled'),  
    }

def getAllChatsForUser(id: str):
    chat_entity = db.Chat

    user_chats = list(chat_entity.find({"participants": id}))
    print(id)

    # Convert each chat to a serializable format
    serialized_chats = [chat_serializer(chat) for chat in user_chats]

    return {"chats":serialized_chats}
