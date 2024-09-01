
from fastapi import APIRouter, HTTPException,Depends, status
from core.models.Chat import Chat
from externals.DB.LLM_model.create import addLLM_model
from core.models.LLM_model import LLM_model


router = APIRouter()

@router.post("/model/add")
async def createModel(
    model:LLM_model
    
):
   
    return addLLM_model(model=model)