from fastapi import  HTTPException
from externals.DB.db_init import db

def model_serializer(model):
    return {
        "name": str(model['name']),
        "description": model.get('description', 'no description'),  
    }

def getAllModelsForUser():
    model_entity = db.Model

    user_models = list(model_entity.find({}))
   

    # Convert each chat to a serializable format
    serialized_model = [model_serializer(model) for model in user_models]

    return {"models":serialized_model}
