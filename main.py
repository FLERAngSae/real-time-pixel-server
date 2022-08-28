import socketio
import json
import asyncio
sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)

def makePixel():
    x = input()
    y = input()
    color = input()
    with open("pixel_color.json") as pixel_json:
        pixel_color = json.load(pixel_json)
    pixel_color[x][y] = color
    with open('data/pixel_color.json', 'w') as f:
        json.dump(pixel_color, f)

makePixel()

@sio.on('connect')
def connect_handler(sid, environ):
	print('connection request')

@sio.on('color')
def color_handler(data: list):
	pass
