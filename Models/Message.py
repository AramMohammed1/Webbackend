from datetime import datetime
from pydantic import BaseModel

class Message(BaseModel):
    content:str
    message_type:str
    message_time:datetime
