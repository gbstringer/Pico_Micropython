# Blinky

Example code to blink an LED

Beginners start here!


## blinky-simple.py

A simple example of how to interact with pins

* Connect an LED to GP1 and GND
* Take care that the longer lead of the LED is connected to GP1
* In this case the outputs are 3.3V so we don't need an additional resistor

## blinky-callback.py

Here we define a function to blink the LED, and call it as part of defining a timer.

* Use the same setup as the simple example.
* This uses an interrupt, which is independent to other code in your program, so you can do other things in the 
code and the LED will continue blinking. 