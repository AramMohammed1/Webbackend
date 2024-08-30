
from fastapi import APIRouter, HTTPException,Depends, status
from fastapi.security import OAuth2PasswordBearer
from core.models.Chat import Chat
from externals. DB.chat.get_one import getChat
from externals. auth.auth import get_current_user
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

oauth2_scheme = HTTPBearer()

router = APIRouter()

@router.get("/chat/{chat_id}")
async def getChatById(
    chat_id: str,
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
    ):
    id = get_current_user(token.credentials)
    return getChat(chat_id=chat_id,userId = id)