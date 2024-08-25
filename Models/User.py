
from Models.Chat import Chat
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password:str
    email: str
    chats:list[Chat]