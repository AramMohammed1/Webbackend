
from fastapi import APIRouter, HTTPException,Depends
from core.models.Chat import Chat
from externals.DB.chat.get_all import getAllChatsForUser
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from externals. auth.auth import get_current_user

oauth2_scheme = HTTPBearer()

router = APIRouter()

@router.get("/user/chats")
async def getAllChats(
        token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
):
    
    id = get_current_user(token.credentials)
    return getAllChatsForUser(id=id)