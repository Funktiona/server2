from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

import socket
import time

s = socket.socket()
# Host local ip
#host = '192.168.1.239' OG Network
#host = '192.168.0.122' # Erik Network
host = '192.168.0.121'
port = 10000
s.bind((host, port))

print(1)
c = None
addr = None

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)


@app.route("/index")
def index():

	return render_template('index.html')

def ret():

	s.listen(5)
	while True:
		print('before')
		c, addr = s.accept()
		print('after')
		print('Got connection from', addr)

	return

# Socket is for reciving direction information
@socketio.on('direction')
def direction(data):

	print(data)

	while True:

		try:


			c.send(data)

			break

		except socket.error, e:

			print(e)

		#c.close()
		#ret()

	#print('before')
	#c, addr = s.accept()
	#print('after')
	#print('Got connection from', addr)

s.listen(5)
while True:
	print('before')
	c, addr = s.accept()
	print('after')
	print('Got connection from', addr)

	break

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)

