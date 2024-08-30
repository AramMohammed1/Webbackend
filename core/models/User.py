
from core.models.Chat import Chat
from pydantic import BaseModel

class User(BaseModel):
    id:str
    username: str
    password:str
    email: str

