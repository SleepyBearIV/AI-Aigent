from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chat_client import ChatClient, Message
from typing import List
from .agent import Agent

app = FastAPI()

# Add CORS middleware for when we later add a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

chat_client = ChatClient()
agent = Agent(chat_client)

@app.get("/heartbeat")
async def heartbeat():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Send to LM Studio through our Agent
        response = await agent.chat(request.message)
        
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
