import adafruit_dotstar # Our LED library
import digitalio
import board
import math
import time
from analogio import AnalogIn


# Set up the pin to read from the microphone
microphone_in = AnalogIn(board.A4)

# These two variables should be adjusted to reflect the number of LEDs you have
# and how bright you want them.
num_pixels = 60
brightness = 0.1

# This creates the instance of the DoTStar library. 
pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, 
    num_pixels, brightness=brightness, auto_write=False)

# Some standard colors. 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)


# This function takes a color and a dely and fills the entire strand with that color. 
# The delay is given in the case you use multiple color fills in a row.  
def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


def get_voltage(pin):
	return (pin.value * 3.3) / 65536



def convert_voltage_to_pixels(raw_voltage):
    num_pixels_to_light = min(int((raw_voltage - 1.59) * 100), 59)
    for pos in range(num_pixels_to_light):
        pixels[pos] = RED 
        pixels.show() 



# ************************************************************************************

color_fill(BLACK,.001)
time.sleep(1)
while True:
	color_fill(BLACK,.001)
	convert_voltage_to_pixels(get_voltage(microphone_in))
	
	
