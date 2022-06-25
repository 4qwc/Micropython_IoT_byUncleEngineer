from machine import Pin
import time

led = Pin(2, Pin.OUT) # LED on bord
sw = Pin(0, Pin.IN) # pin sw onbord

def handle_interrupt(pin):
    led.value(not led.value())

sw.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)