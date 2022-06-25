from machine import Pin
import time

led = Pin(2, Pin.OUT) # LED on bord
sw = Pin(0, Pin.IN) # pin sw onbord

def blink_led(num, t_on, t_off, msg):
    counter = 0
    while(counter < num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter += 1
    print(msg)
    
while True:
    if(sw.value()==0): # if value = 0
        blink_led(10,0.10,0.10,'END')
