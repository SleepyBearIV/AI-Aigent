from typing import Dict, Optional
from .base import BaseTool
from .webb_tool import WebSearchTool

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}

    def register_tool(self, tool: BaseTool) -> None:
        """Register a new tool in the registry."""
        self._tools[tool.name] = tool

    def get_tool(self, name: str) -> Optional[BaseTool]:
        """Get a tool by its name, returns None if not found."""
        return self._tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        """Get all available tools as name -> description mapping."""
        return {name: tool.description for name, tool in self._tools.items()}

    async def execute_tool(self, name: str, query: str) -> Optional[str]:
        """Execute a tool by name with the given query."""
        tool = self.get_tool(name)
        if tool is None:
            return None
        return await tool.execute(query)

def create_default_registry() -> ToolRegistry:
        """Create a registry with all default tools registered."""
        registry = ToolRegistry()
        registry.register_tool(WebSearchTool())
        return registry

# In your agent later:
registry = create_default_registry()
# Now registry has your web_search tool ready to use