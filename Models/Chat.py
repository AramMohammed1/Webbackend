
from pydantic import BaseModel
from typing import List
from Models.Message import Message  # Adjust the import path as necessary
from datetime import datetime


class Chat(BaseModel):
    participants: List[str]  # List of participant user emails or IDs
    created_at: datetime  # Timestamp for when the chat was created
    title:str