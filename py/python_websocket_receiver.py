import asyncio
import websockets

async def hello(websocket, path):
    hr = await websocket.recv()
    print(f"< {hr}")

    # greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    print(f"got heartrate")

start_server = websockets.serve(hello, "127.0.0.1", 927)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()