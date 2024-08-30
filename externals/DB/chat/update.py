from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
from bson import ObjectId
from externals.DB.db_init import db
from core.models.Config import Config
import httpx
from dotenv import load_dotenv
import os
load_dotenv()
ragHost = os.getenv('RAGBASEURL')


def updateChat(chat_id: str,
    config:Config
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
                "chunks":config.chunks,
                "numofresults": config.numofresults,
            }
        }
    )
    



    return {"message": "Chat updated successfully"}





async def updateChatFiles(    chat_id: str,

    files: List[UploadFile]=File(...)
):
    chat_entity = db.Chat
    chat_object_id = ObjectId(chat_id)

    # Find the chat by chat_id
    chat = chat_entity.find_one({"_id": chat_object_id})
    
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    file_paths = []
    files_to_upload = []
    for file in files:
        print(file.filename)
        file_paths.append(file.filename)
        files_to_upload.append(("files", (file.filename,await file.read(), file.content_type)))

    print(chat_object_id)
    # Update the chat document with the new data
    update_result = chat_entity.update_one(
        {"_id": chat_object_id},
        {
            "$set": {
                "fileName": file_paths,  # Save file paths if needed
            }
        }

    )
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(
                ragHost+"api/uploadfile/",
                files=files_to_upload
            )
            response.raise_for_status()  # Raises an error for 4xx/5xx responses

            print("External service response status code:", response.status_code)
            print("External service response content:", response.text)



        except httpx.HTTPStatusError as e:
            print("HTTPStatusError:", e)
            raise HTTPException(status_code=e.response.status_code, detail="Failed to notify external service")
        except Exception as e:
            print("General Exception:", repr(e))  # Use repr to capture the full exception details
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


    return {"message": "Chat updated successfully"}