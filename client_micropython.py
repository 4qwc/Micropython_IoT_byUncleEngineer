import network
wifi = 'Kannatham_2022'
password = 'Kannatham2022'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(wifi, password)
print(wlan.isconnected())

if wlan.isconnected():
    print('connected')
    

wlan.ifconfig()

import socket
serverip = '192.168.1.39'
port = 9000

def send_data(data):
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))
	data_server = server.recv(1024).decode('utf-8')
	print('Server:' , data_server)
	server.close()
	
send_data('Hello Macbook')