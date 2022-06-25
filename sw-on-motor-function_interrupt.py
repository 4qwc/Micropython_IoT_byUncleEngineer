from machine import Pin
import time

# set pin INPUT - OUTPUT
sw1 = Pin(15, Pin.IN, Pin.PULL_UP)
sw2 = Pin(21, Pin.IN, Pin.PULL_UP)
dr1 = Pin(22, Pin.OUT)
dr2 = Pin(23, Pin.OUT)

press = False
irq_pin = 0

def handle_interrupt(pin):
    global press
    press = True
    global irq_pin
    irq_pin = int(str(pin)[4:1])

# set interrupt input
sw1.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)
sw2.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
    if press:
        print(irq_pin)
        press = False
        
        if ira_pin == 15:
            dr1.value(0)
            dr2.value(1)
            print('counter')
        elif irq_pin == 21:
            dr1.value(1)
            dr2.value(0)
            print('clockwise')
        else:
            pass
