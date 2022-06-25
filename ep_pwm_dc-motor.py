from machine import Pin

dr1 = Pin(21, Pin.OUT)
dr2 = Pin(19, Pin.OUT)

en1 = Pin(18, Pin.OUT)

def cw():
    dr1.value(0)
    dr2.value(1)
    
def ccw():
    dr1.value(1)
    dr2.value(0)
    
def start(rotation):
    pwm.init(freq=1, duty=512)
    if(ritation=='cw'):
        cw()
    elif(rotation=='ccw'):
        ccw()
    
    
    