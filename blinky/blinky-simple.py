from machine import Pin
import time

led = Pin(1, Pin.OUT)

while True:
    led.toggle()
    time.sleep_ms(200)	# 200 ms = 1/5 second