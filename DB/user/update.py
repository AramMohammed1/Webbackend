from backend.DB.db_init import db
from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter ,HTTPException
from Models.User import User
from pydantic import BaseModel, EmailStr
router=APIRouter()

@router.post("/user/update")
async def updateUser(user: User):
  # Build the update data
    update_data = {}
    if user.name:
        update_data["name"] = user.name
    if user.password:
        update_data["password"] = user.password  # Consider hashing the password here

    # If no update data is provided, raise an error
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided to update")

    # Update the user by email
    update_result = db.User.update_one({"email": user.email}, {"$set": update_data})

    # Check if the user was found and updated
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    if update_result.modified_count == 0:
        return {"message": "No changes were made to the user"}

    return {"message": "User updated successfully"}