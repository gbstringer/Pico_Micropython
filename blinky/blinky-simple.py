from machine import Pin	# import the definitions for interacting with pins (GPn)
import time				# load the 'time' library, which has lots of time-related functions

led = Pin(1, Pin.OUT)	# define a pin for output

while True:				# do this forever!
    led.toggle()		# toggle the led pin
    time.sleep_ms(200)	# pause for 200 ms = 1/5 second