import socket
import network
import time
from machine import Pin
import dht
#####################
# serverip = '178.128.125.82'
serverip = '192.168.1.39'
port = 9009
#####################

def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()
'''
########WIFI########
wifi = 'Kannatham_2.4GHz'
password = 'Kannatham[2022]'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2) # delay 2 seconds
wlan.connect(wifi, password)
time.sleep(2)
print(wlan.isconnected())
'''

#
# connect wifi auto
wifi = 'Kannatham_2.4GHz'
password = 'Kannatham[2022]'
wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.active(True)
    wlan.connect(wifi, password)
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())
print(wlan.isconnected())
#******************************************

####################

#send_data('Hello-IOT - PROJECT')

print('> Temperature cheking...')
d = dht.DHT22(Pin(16))


for i in range(100):
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humi = d.humidity()
    print('TEMP:',temp)
    print('HUMI',humi)
    #text = 'TEMP-HUMID: {} and {}'.format(Temp,Humi)
    text = 'TEMP:{}'.format(temp)# send data temp
    send_data(text)
    time.sleep(3)
    print('------')
    