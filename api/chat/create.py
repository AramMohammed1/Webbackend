
from fastapi import APIRouter, HTTPException,Depends, status
from fastapi.security import OAuth2PasswordBearer
from core.models.Chat import Chat
from externals.DB.chat.create import addChat
from externals.auth.auth import get_current_user
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

oauth2_scheme = HTTPBearer()

router = APIRouter()

@router.post("/chat/add")
async def createChat(
    chat:Chat,
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
):
    id = get_current_user(token.credentials)
    chat.participants.append(id)
    return addChat(chat=chat)