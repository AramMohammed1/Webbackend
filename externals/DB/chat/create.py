from externals.DB.db_init import db
from core.models.Chat import Chat

def addChat(
   chat:Chat
):
    chat_entity = db.Chat
    if not chat.title.strip():
       chat.title = "Untitled"

    # Insert the new chat into the database
    chat_entity.insert_one({"participants":chat.participants,
                          "title":chat.title,
                          "created_at":chat.created_at
                            })

    return {"message": "Chat added successfully"}
