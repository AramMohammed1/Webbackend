from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat.get_all import router as getallChatRouter
from api.chat.create import router as createChatRouter
from api.chat.get_one import router as getChatRouter
from externals.DB.user.verfiy import router as verfiyUser
from externals.DB.user.delete import router as deleteUser
from api.message.create import router as createMessage
from api.chat.update import router as updateChat
from api.auth.auth import router as auth
app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(getallChatRouter)
app.include_router(createChatRouter)
app.include_router(getChatRouter)
app.include_router(verfiyUser)
app.include_router(deleteUser)
app.include_router(createMessage)
app.include_router(updateChat)
app.include_router(auth)