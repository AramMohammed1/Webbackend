from fastapi import APIRouter,Depends,UploadFile, File
from core.models.Message import Message
from externals.DB.message.create import addMessage
from externals.auth.auth import get_current_user
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


oauth2_scheme = HTTPBearer()

router = APIRouter()

@router.post("/chat/{chat_id}/add_message")
async def addNewMessage(
    chat_id: str,
    message: Message,
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)

):
    get_current_user(token.credentials)
    return await addMessage(chat_id,message)