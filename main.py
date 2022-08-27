import socketio
import asyncio
sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)

@sio.on('connect')
def connect_handler(sid, environ):
	print('connection request')

@sio.on('color')
def color_handler(data: list):
	pass