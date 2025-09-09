from typing import List, Dict, Any
from urllib import response
import aiohttp
import json
from dotenv import load_dotenv
import os


class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
class ChatClient:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))
        self.max_tokens = int(os.getenv("MAX_TOKENS", 2000))

    async def chat(self, messages: List[Message]) -> str:
        async with aiohttp.ClientSession() as session:
            try:
                request_body = {
                    "model": "openai/gpt-oss-20b",  # The model name from LM Studio
                    "messages": [
                        {"role": msg.role, "content": msg.content}
                        for msg in messages
                    ],
                    "temperature": self.temperature,
                    "max_tokens": self.max_tokens
                }
                
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    json=request_body
                ) as response:
                    response.raise_for_status()
                    result = await response.json()
                    return result["choices"][0]["message"]["content"]
            except aiohttp.ClientError as e:
                raise Exception(f"API request failed: {e}")