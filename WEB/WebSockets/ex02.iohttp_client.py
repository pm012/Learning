import asyncio
import aiohttp


async def client():
    # session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.get("https://gittrrrrh.com", timeout=10)

            if response.ok:
                body = await response.text()
                print(body[:400])
            else:
                print("Not okay")
        except asyncio.TimeoutError as e:
            print(f"{e}")
        except aiohttp.ClientConnectionError as e:
            print(f"{e}")
        


if __name__ == '__main__':
    asyncio.run(client())
