from machine import Pin
import dht
import time
d = dht.DHT22(Pin(16))
d.measure()

Temp = d.temperature()
Humi = d.humidity()

for i in range(100):
    d.measure()
    time.sleep(1)
    
    print('TEMP:',Temp)
    print('HUMI:',Humi)
    print('------------')
    time.sleep(3)
