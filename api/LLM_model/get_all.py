
from fastapi import APIRouter, HTTPException,Depends
from core.models.Chat import Chat
from externals.DB.LLM_model.get_all import getAllModelsForUser
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from externals. auth.auth import get_current_user

oauth2_scheme = HTTPBearer()

router = APIRouter()

@router.get("/get/models")
async def getAllModels(
        token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
):
    
    id = get_current_user(token.credentials)
    return getAllModelsForUser()