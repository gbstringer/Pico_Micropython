from machine import Pin, Timer
import time

led = Pin(1, Pin.OUT)


timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=1, mode=Timer.PERIODIC, callback=blink)