from pydantic import BaseModel

class LLM_model(BaseModel):
    name:str
    url:str
    description:str