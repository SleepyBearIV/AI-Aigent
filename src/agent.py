from typing import List, Dict, Any, Callable
from chat_client import ChatClient, Message
import re

class Tool:
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

    
class Agent:
    def __init__(self, chat_client: ChatClient):
        self.chat_client = chat_client
        self.tools: Dict[str, Tool] = {}
    def register_tool(self, name: str, description: str, func: Callable):
        self.tools[name] = Tool(name, description, func)

    def _create_system_prompt(self) -> str:
        pass

    async def chat(self, user_input: str) -> str:
        messages = [
            Message("system", self._create_system_prompt()),
            Message("user", user_input)
        ]
        while True:
            response = await self.chat_client.chat(messages)
            if "TOOL:" in response:
                tool_match = re.search(r"TOOL: (\w+)\nINPUT: (.+?)(?=\n|$)", response)
                if tool_match:
                    tool_name = tool_match.group(1)
                    tool_input = tool_match.group(2).strip()
                    tool = self.tools.get(tool_name)
                    if tool_name in self.tools:
                        tool_result = self.tools[tool_name].func(tool_input)
                        messages.append(Message("assistant", response))
                        messages.append(Message("user", f"Observation: {tool_result}"))
                        continue