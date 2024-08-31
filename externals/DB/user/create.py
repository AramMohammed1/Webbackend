from externals.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from core.models.User import User
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext



def addUser(user:User):
    entity=db.User
    
    entity.insert_one({"name":user.username,"password":user.password,"email":user.email})
    return {"message": "User added successfully"}
