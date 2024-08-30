
from pydantic import BaseModel
from typing import List
from core.models.Message import Message  # Adjust the import path as necessary
from datetime import datetime



class Chat(BaseModel):
    participants: List[str]=[]
    created_at: datetime 
    title:str
    messages:List [Message]=[]
    chunks:int =500
    numofresults:int =1
    fileNames:List[str] = [""] 