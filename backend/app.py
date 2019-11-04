import aiohttp_cors

from aiohttp import web
from sudoku_generator import grid, sudoku_generator

routes = web.RouteTableDef()


@routes.get('/')
async def on_get(request):

    example = grid.grid()
    example.mix()
    difficult = example.n ** 4  # Первоначально все элементы на месте
    solved = example.show()
    sudoku_generator.generate(difficult, example)
    generated = example.show()
    return web.json_response({
        'solved': solved,
        'generated': generated
    })

app = web.Application()
app.add_routes(routes)

# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=8081)
