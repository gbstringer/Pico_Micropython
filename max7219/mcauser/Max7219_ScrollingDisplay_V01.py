'''
 Demonstrates the use of MAX7219, Scrolling display.
 
 * Demonstrate to display the scrolling display.
 * Four numbers of the MAX7219 are connected in daisy chain.
 * 8x8 dot matrix module, (64 LEDs) is connected with each MAX7219
 * totally 8x8x4 = 256 LEDs forming with 8 rows of 32 columns Display area.
 
 * The Raspberry Pi Pico pin connections are MAX7219 given below:

 * MAX7219 VCC pin to VBUS
 * MAX7219 GND pin to GND
 * MAX7219 DIN pin to digital GPIO3
 * MAX7219 CS pin to digital GPIO5
 * MAX7219 CLOCK pin to digital GPIO2

 Name:- M.Pugazhendi
 Date:-  10thJul2021
 Version:- V0.1
 e-mail:- muthuswamy.pugazhendi@gmail.com
'''

# Import MicroPython libraries of PIN and SPI
from machine import Pin, SPI

# Import MicoPython max7219 library
import max7219

# Import time
import time

#Intialize the SPI
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

# Create matrix display instant, which has four MAX7219 devices.
display = max7219.Matrix8x8(spi, ss, 4)

#Set the display brightness. Value is 1 to 15.
display.brightness(10)

#Define the scrolling message
scrolling_message = "RASPBERRY PI PICO AND MAX7219 -- 8x8 DOT MATRIX SCROLLING DISPLAY"

#Get the message length
length = len(scrolling_message)

#Calculate number of columns of the message
column = (length * 8)

#Clear the display.
display.fill(0)
display.show()

#sleep for one one seconds
time.sleep(1)

# Unconditionally execute the loop
while True:
    for x in range(32, -column, -1):     
        #Clear the display
        display.fill(0)

        # Write the scrolling text in to frame buffer
        display.text(scrolling_message ,x,0,1)
        
        #Show the display
        display.show()
      
        #Set the Scrolling speed. Here it is 50mS.
        time.sleep(0.05)