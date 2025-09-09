import aiohttp
import json
from .base import BaseTool

class WebSearchTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Search the web for current information and news"
        )

    async def execute(self, query: str) -> str:
        """Execute web search and return formatted results."""
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "engine": "duckduckgo",
                "no_redirect": 1,
                
            }
            print(query)

            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                async with session.get(url, params=params) as response:
                    response.raise_for_status()
                    content_type = response.headers.get('content-type', '')
                    # Just get whatever DuckDuckGo sends and print it
                    raw_data = await response.text()
                    print("=== DUCKDUCKGO RESPONSE ===")
                    print(raw_data)
                    print("=== END RESPONSE ===")
                    return raw_data
        except Exception as e:
            return f"An error occurred: {str(e)}"



