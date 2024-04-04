from aiohttp import web

from logger import logger


async def index(request):
    try:
        logger.debug(f"{request.path=}")
        file_path = request.path[1:]
        logger.debug(f"{file_path=}")
        if not file_path:
            file_path = 'index.html'

        content_type = 'text/html'
        if file_path.endswith('.css'):
            content_type = 'text/css'
        elif file_path.endswith('.js'):
            content_type = 'application/javascript'

        logger.debug(f"{content_type=}")

        with open(f'public/{file_path}', 'rb') as file:
            return web.Response(body=file.read(), content_type=content_type)

    except FileNotFoundError:
        return web.Response(status=404)

if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/{tail:.*}', index)

    web.run_app(app, host="localhost", port=8080)
