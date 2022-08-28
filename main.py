import socketio
import json
import asyncio
sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)

def makePixel(x: str, y: str, color: str):
    with open("data/pixel_color.json") as pixel_json:
        pixel_color = json.load(pixel_json)
    pixel_color[x][y] = color
    with open('data/pixel_color.json', 'w') as f:
        json.dump(pixel_color, f)
    return pixel_color

makex = input()
makey = input()
makec = input()
makePixel(makex, makey, makec)

@sio.on('connect')
def connect_handler(sid, environ):
	print('connection request')

@sio.on('change')
def color_handler(x: str, y: str, color: str):
    pc = makePixel(x, y, color)
    sio.emit('update', pc)

