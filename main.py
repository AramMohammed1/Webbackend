from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from DB.chat.get_all import router as getallChatRouter
from DB.chat.create import router as createChatRouter
from DB.chat.get_one import router as getChatRouter
from DB.user.create import router as createUser
from DB.user.verfiy import router as verfiyUser
from DB.user.delete import router as deleteUser
from DB.message.create import router as createMessage
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
app.include_router(createUser)
app.include_router(verfiyUser)
app.include_router(deleteUser)
app.include_router(createMessage)