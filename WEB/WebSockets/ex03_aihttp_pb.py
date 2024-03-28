import asyncio
from aiohttp import ClientSession, ClientConnectionError
from datetime import datetime
import logging


URL = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
URL_NBU = "" #TODO

async def request(url:str):
    async with ClientSession() as session:
        try: 
            async with session.get(url) as resp:
                if resp.ok:
                    r = await resp.json()
                    return r
                logging.error(f"Error status: {resp.status} for {url}")
                return None
        except ClientConnectionError as err:
            logging.error(f"Connection error:{str(err)}")
            return None
        
def bp_handler(result):
    exc, = list(filter(lambda el: el["ccy"]=="USD", result))
    return f"USD: buy: {exc['buy']}, sale: {exc['sale']}, Date: {datetime.now().date()}"

def nbu_handler(result):
    return result[0]
        
async def get_exchange(url, handler):
    result = await request(url)
    if result:
        
        return handler(result)
    return "Failed to retrieve data"
    

    
        


if __name__ == "__main__":
    result = asyncio.run(get_exchange(URL, bp_handler))
    print(result)
    #TODO add nbu handler call
