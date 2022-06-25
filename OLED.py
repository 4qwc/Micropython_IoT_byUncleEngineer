from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32
# i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
# ESP8266
i2c = SoftI2C(sda=Pin(4) ,scl=Pin(5)) # SDA=D2, SCL=D1

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width,oled_height, i2c)

oled.text('Hello, World 1',0, 5)
oled.text('Hello,HS4QWC!!!',0,20)
oled.text('Hello world! 3',0,40)

#oled.fill(1) # 0=เติมสีหน้าจอดำ ,1=ใส่สีหน้าจอ
oled.invert(True) # เติมสีพื้นหลัง
oled.show() # แสดงผลหน้าจอ