from machine import Pin, SPI
import max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(10)

while True:

    display.fill(0)
    display.text('MICR',0,0,1)
    display.show()
    sleep(3)

    display.fill(0)
    display.text('DIGI',0,0,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('SOFT',0,0,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('PICO',0,0,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('DONE',0,0,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('1234',0,0,1)
    display.show()
    sleep(3)