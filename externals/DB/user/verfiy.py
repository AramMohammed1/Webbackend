from externals.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from core.models.User import User
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
router=APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post("/user/verify")
async def verifyUser(user: User):
    # Find user by email
    db_user = db.User.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Verify the password
    is_password_valid = pwd_context.verify(user.password, db_user["password"])
    if not is_password_valid:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"message": "User verified successfully"}