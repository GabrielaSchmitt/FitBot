from fastapi import FastAPI
from pydantic import BaseModel
import os
from pymongo import MongoClient

app = FastAPI()

# Conectar ao MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_database()
messages_collection = db.messages

class Message(BaseModel):
    from_: str
    text: str
    timestamp: str

@app.post("/a")
async def testing():
    return {"status": "success", "message": "acessed."}

@app.post("/webhook")
async def webhook(message: Message):
    if message.text.startswith("fitbot"):
        user_message = message.text.replace("fitbot", "").strip()
        user_number = message.from_
        messages_collection.insert_one({
            "user": user_number,
            "message": user_message,
            "timestamp": message.timestamp
        })
        return {"status": "success", "message": "Data saved."}
    return {"status": "error", "message": "No valid message received."}
