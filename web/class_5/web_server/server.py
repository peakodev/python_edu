from aiohttp import web


async def index(request: web.Request) -> web.Response:
    with open("index.html") as f:
        body = f.read()
    return web.Response(body=body, status=200, content_type='text/html')


async def hello_html(request):
    return web.Response(
        content_type='text/html',
        body="<h1>Hello</h1>",
        status=200)


async def hello_json(request):
    return web.Response(
        content_type='application/json',
        body=['2', '22'],
        status=200)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([
        web.get('/', index),
        web.get('/hello_html', hello_html),
        web.get('/hello_json', hello_json),
    ])
    web.run_app(app)
