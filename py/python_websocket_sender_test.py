import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://127.0.0.1:927/') as websocket:
        await websocket.send('80')

asyncio.get_event_loop().run_until_complete(hello())