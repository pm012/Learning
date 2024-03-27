import asyncio
import requests
from pprint import pprint as print
from concurrent.futures import ThreadPoolExecutor

from async_util import async_timeit




urls = ['http://www.google.com', 
        'http://www.python.org', 
        'http://duckduckgo.com', 
        'http://www.google.com',
        'ttt',
        'http://www.python.org', 
        'http://duckduckgo.com', 
        'http://www.google.com', 
        'http://www.python.org/fake'
        ]


def get_url(url:str)->tuple[str:str]: # Blocking IO operation
    r = requests.get(url)
    return url, r.text[:100]

@async_timeit
async def get_url_async():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(8) as pool:
        features = [loop.run_in_executor(pool, get_url, url) for url in urls]
        r = await asyncio.gather(*features,return_exceptions=True) # If return exception is set to False or the parameter was not set it results in throwing exception and ending the execution
        print(r)

if __name__ == '__main__':
    asyncio.run(get_url_async())

    # try:
    #     for url in urls:
    #         print(get_url(url))
    # except requests.exceptions.MissingSchema as e:
    #     print(e)

