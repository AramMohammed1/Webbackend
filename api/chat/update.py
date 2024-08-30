
from fastapi import APIRouter,Depends,UploadFile, File
from core.models.Config import Config
from externals.DB.chat.update import updateChat
from externals.DB.chat.update import updateChatFiles
from externals.auth.auth import get_current_user
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import List

oauth2_scheme = HTTPBearer()
router = APIRouter()
@router.post("/chat/{chat_id}/update")
async def updateChatById(chat_id: str,
    config:Config,
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
):
    get_current_user(token.credentials)
    return updateChat(chat_id,config)
    


@router.post("/chat/{chat_id}/updatefile")
async def update_chat_files(    chat_id: str,
    files: List[UploadFile]=File(...),
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)
):
    id= get_current_user(token.credentials)
    return await updateChatFiles(chat_id,files)