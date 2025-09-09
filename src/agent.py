from typing import List, Dict, Any, Callable
from .chat_client import ChatClient, Message
import re
from .tools.registry import ToolRegistry, create_default_registry
import json


    
class Agent:
    def __init__(self, chat_client: ChatClient):
        self.chat_client = chat_client
        self.registry = create_default_registry()


    def _create_system_prompt(self) -> str:
        tools_info = self.registry.list_tools()
        tool_list = "\n".join([f"- {name}: {desc}" for name, desc in tools_info.items()])
        return f"""You are a helpful AI assistant with access to these tools:

{tool_list}

When you need to use a tool, respond with ONLY a JSON object in this format:
{{"action": "use_tool", "tool_name": "web_search", "query": "your search query"}}

Otherwise, respond normally to help the user."""

    async def chat(self, user_input: str) -> str:
        messages = [
            Message("system", self._create_system_prompt()),
            Message("user", user_input)
        ]

        while True:
            response = await self.chat_client.chat(messages)


            # Check if response contains JSON wrapped in channel format
            if "<|message|>" in response:
                # Extract JSON part after <|message|>
                json_start = response.find("<|message|>") + len("<|message|>")
                json_part = response[json_start:]

                try:
                    parsed = json.loads(json_part)
                    print(1)
                    if parsed.get("action") == "use_tool":
                        print(2)
                        tool_name = parsed.get("tool_name")
                        query = parsed.get("query")
                        if tool_name and query is not None:
                            result = await self.registry.execute_tool(tool_name, query)
                            if result:
                                messages.append(Message("assistant", response))
                                messages.append(Message("user", f"Tool result: {result}"))
                                continue
                            else:
                                return f"Error: Tool '{tool_name}' failed to execute."
                        else:
                            return f"Error: Missing tool_name or query in request."
                    else:
                        return f"Error: Unknown action '{parsed.get('action')}'. Expected 'use_tool'."
                except json.JSONDecodeError:

                    return response