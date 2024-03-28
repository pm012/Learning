from  aiohttp import web
import asyncio


async def index(request):
    return web.Response(body="<h1>Hello from index<h1>", 
                        status = 200,
                        content_type="text/html")

async def hello(request):
    return web.Response(body="Hello from hello", status=200)



if  __name__ =='__main__':
    app = web.Application()
    app.add_routes([web.get("/", index), web.get("/hello", hello)])
    web.run_app(app, host="127.0.0.1")