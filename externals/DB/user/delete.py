from externals.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from core.models.User import User
from pydantic import BaseModel, EmailStr
router=APIRouter()



@router.post("/user/delete")
async def deleteUser(user:User):
    entity=db.User
    chat_entity=db.Chat

    delete_result = entity.delete_one({"email": user.email})
# Check if the user was found and deleted
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    chat_entity.delete_many({"user_email":user.email})
    return {"message": "User deleted successfully"}
