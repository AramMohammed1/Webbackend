from backend.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from Models.User import User
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
router=APIRouter()




# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/user/add")
async def addUser(user:User):
    entity=db.User

    # Hash the user's password
    hashed_password = pwd_context.hash(user.password)

    entity.insert_one({"name":user.name,"password":hashed_password,"email":user.email,"chats": [] 
                       
                       })
    return {"message": "User added successfully"}
