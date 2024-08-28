from fastapi import APIRouter, HTTPException, UploadFile, File,Form
from typing import List
from bson import ObjectId
from DB.db_init import db
from pydantic import BaseModel

router = APIRouter()
class UpdateChatRequest(BaseModel):
    chunks: int
    numofresults: int
    files:List[UploadFile]
@router.post("/chat/{chat_id}/update")
async def updateChat(    chat_id: str,
    chunks: int = Form(...),
    numofresults: int = Form(...),
):
    chat_entity = db.Chat
    chat_object_id = ObjectId(chat_id)

    # Find the chat by chat_id
    chat = chat_entity.find_one({"_id": chat_object_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
 
    
    # Update the chat document with the new data
    update_result = chat_entity.update_one(
        {"_id": chat_object_id},
        {
            "$set": {
                "chunks": chunks,
                "numofresults": numofresults,
            }
        }
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=500, detail="Failed to update chat")
    
    return {"message": "Chat updated successfully"}





@router.post("/chat/{chat_id}/updatefile")
async def updateChatFiles(    chat_id: str,

    files: List[UploadFile]
):
    chat_entity = db.Chat
    chat_object_id = ObjectId(chat_id)

    # Find the chat by chat_id
    chat = chat_entity.find_one({"_id": chat_object_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    file_paths = []
    for file in files:
        file_paths.append(file.filename)
    
    # Update the chat document with the new data
    update_result = chat_entity.update_one(
        {"_id": chat_object_id},
        {
            "$set": {
                "fileName": file_paths,  # Save file paths if needed
            }
        }
    )

    if update_result.modified_count == 0:
        raise HTTPException(status_code=500, detail="Failed to update chat")
    
    return {"message": "Chat updated successfully"}