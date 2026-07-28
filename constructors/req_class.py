import httpx
import asyncio

class RequestClass:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def get_response(self, link: str):
        return await self.client.get(link, follow_redirects=True)

    async def close(self):
        await self.client.aclose()