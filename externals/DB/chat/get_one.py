from externals.DB.db_init import db
from fastapi import HTTPException
from bson import ObjectId  # Import ObjectId to convert string to ObjectId

def getChat(chat_id: str,userId:str):
    chat_entity = db.Chat
    try:
        chat_object_id = ObjectId(chat_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid chat ID format")
    chat = chat_entity.find_one({"_id": chat_object_id})
    isInChat = False
    for ch in chat["participants"]:
        if(ch==userId):
            isInChat=True
            break
    if not isInChat:
        raise HTTPException(status_code=404, detail="Unauthorized")
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    chat['_id'] = str(chat['_id'])
    # Return the chat data
    return chat

