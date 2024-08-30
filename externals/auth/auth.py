from datetime import datetime, timedelta, timezone
from typing import Annotated

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



SECRET_KEY = "23c3aae4af8e824a3d6b14d2eefc50843d0db04fba01206e68af5486d78d68dc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = HTTPBearer()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def get_current_user(token: HTTPAuthorizationCredentials=  Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except InvalidTokenError:
        raise credentials_exception
    return id


def authenticate_user(email: str, password: str):
    user = getUser(email)
    if not user:
        raise HTTPException(status_code=400, detail="User Not Found or Incorrect Password")
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="User Not Found or Incorrect Password")
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt








