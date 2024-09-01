from externals.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from core.models.LLM_model import LLM_model
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext



def addLLM_model(model:LLM_model):
    entity=db.Model
    
    entity.insert_one({"name":model.name,"url":model.url,"description":model.description})
    return {"message": "User added successfully"}
