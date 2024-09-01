from pydantic import BaseModel

class Config(BaseModel):
    chunks: int 
    numofresults: int 
    modelname:str
