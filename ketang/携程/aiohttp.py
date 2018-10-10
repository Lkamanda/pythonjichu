from aiohttp import web
import asyncio
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init (loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop .create_server(app.make_handler().)