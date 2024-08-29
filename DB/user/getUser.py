from DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from Models.User import User
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

def getUser(email:str):
    entity = db.User

    user = entity.find_one({"email":email})
    return user
