import platform
import aiohttp
import asyncio
from uuid import uuid4

async def main():
    timemout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(
        headers={"Reqest-Id": str(uuid4())}, timeout=timemout,) as session:
            async with session.get('https://python.org') as response:
                  print("Status:", response.status )    
                  print("Content-type:", response.headers['content-type'])
                  #print("Request-id:", response.headers(['Request-Id']))
                  print(response.headers)

                  html = await response.text()
                  return f"Body: {html[:15]}..."
if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    r = asyncio.run(main())
    print(r)

                