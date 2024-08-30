

from fastapi import Depends,APIRouter,HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
from core.models.User import User
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from externals.DB.user.getUser import getUser
from externals.DB.user.create import addUser
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from externals.auth.auth import *
from core.models.SignUp import SignUp
oauth2_scheme = HTTPBearer()
router = APIRouter()


@router.post("/users/login")
async def login(
    email:str,password:str
):
    user = authenticate_user(email,password)
    
    accessToken = create_access_token(
        {
            "id":str(user['_id']),
        }
    )
    return accessToken
    
@router.post("/users/signup")
async def signup(model:SignUp):
    hash_password = get_password_hash(model.password)
    user = User(id="",username=model.email, email=model.email ,password=hash_password)
    print(addUser(user))
    return {"message":"ok"}

