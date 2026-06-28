import os
from urllib import response

from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel

# Load env variables
load_dotenv()

# create fastAPI app
app= FastAPI()

# create groq client
client= Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# body model
class ChatRequest(BaseModel):
    messages: str

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# Chat route
@app.post("/chat")
def chat(request: ChatRequest):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": request.messages
            }
        ]
    )
    print("User:", request.messages)
    print("AI:", response.choices[0].message.content)
    return {"response": response.choices[0].message.content}
