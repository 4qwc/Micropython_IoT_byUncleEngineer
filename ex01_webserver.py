#x01_webserver.py
'''
Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection
'''


from machine import Pin
import network
#import wifi_my
import socket

led = Pin(2, Pin.OUT)

ssid = 'Kannatham_2.4GHz'
password = 'Kannatham[2022]'


# connect wifi
#******************************************
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
print('status:',wlan.isconnected())
#******************************************