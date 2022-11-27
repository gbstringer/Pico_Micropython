# Example showing use of HSV colors
import time
from neopixel import Neopixel

colours_dict = {
    "red":    (255,0,0),
    "orange": (255,180,0),
    "yellow": (200,200,20),
    "green":  (0,255,0),
    "blue":   (0,0,255),
    "indigo": (0,0,128),
    "violet": (63,0,127),
    "black":  (0,0,0),
    }

numpix = 8
strip = Neopixel(numpix, 0, 0, "GRB")

while(True):
    
    for pixel in range(8):
        for colname,colvalue in colours_dict.items():
            strip.set_pixel(pixel,colvalue)
            print(pixel,colname,colvalue)
        strip.show()
        time.sleep(0.2)
    
    strip.fill((0,0,0))
    strip.show
    time.sleep(1)
