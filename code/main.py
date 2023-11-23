import adafruit_dotstar # Our LED library
import digitalio
import board
import math
import time

print("LumiDrive v10") 

# Setting up the product's blue stat LED to blink
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

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

# A list of the ten colors. Use this if you want to cycle through the colors. 
colorList = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE]

# The travel function takes a color and the time between updating the color. It
# will start at LED one on the strand and fill it with the give color until it
# reaches the maximum number of pixels that are defined as "num_pixels".
def travel(color, wait):
    num_pixels = len(pixels)
    for pos in range(num_pixels):
        pixels[pos] = color 
        pixels.show() 
        time.sleep(wait)

# This function takes a color and a dely and fills the entire strand with that color. 
# The delay is given in the case you use multiple color fills in a row.  
def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


def show_all_pieces():
	color_fill(BLACK,.001) 


	# Mouth
	pixels[0] = RED
	pixels[1] = RED
	pixels[2] = RED
	pixels[3] = RED

	# Soul Patch
	pixels[4] = RED
	pixels[5] = RED
	pixels[6] = RED

	# Right Cheek
	pixels[7] = WHITE
	pixels[8] = BLACK
	pixels[9] = BLACK
	pixels[10] = WHITE

	# Right Eye
	pixels[11] = PURPLE
	pixels[12] = PURPLE
	pixels[13] = PURPLE

	# Right Eyebrow
	pixels[14] = WHITE

	# Large Brow
	pixels[15] = RED
	pixels[16] = RED
	pixels[17] = RED
	pixels[18] = RED
	pixels[19] = RED
	pixels[20] = RED
	pixels[21] = RED
	pixels[22] = RED

	# Small Brow
	pixels[23] = RED
	pixels[24] = RED
	pixels[25] = RED
	pixels[26] = RED
	pixels[27] = RED
	pixels[28] = RED
	pixels[29] = RED

	# Forehead & Left Eyebrow
	pixels[30] = WHITE
	pixels[31] = BLACK
	pixels[32] = BLACK
	pixels[33] = BLACK
	pixels[34] = BLACK
	pixels[35] = BLACK
	pixels[36] = WHITE
	pixels[37] = BLACK
	pixels[38] = BLACK
	pixels[39] = WHITE

	# Left Eye
	pixels[40] = PURPLE
	pixels[41] = PURPLE
	pixels[42] = PURPLE

	# Left Cheek
	pixels[43] = WHITE
	pixels[44] = BLACK
	pixels[45] = BLACK
	pixels[46] = WHITE


	pixels.show()



def stop_speaking():
	color_fill(BLACK,.001) 


	# Mouth
	pixels[0] = BLACK
	pixels[1] = BLACK
	pixels[2] = BLACK
	pixels[3] = BLACK

	# Soul Patch
	pixels[4] = BLACK
	pixels[5] = BLACK
	pixels[6] = BLACK

	# Right Cheek
	pixels[7] = WHITE
	pixels[8] = BLACK
	pixels[9] = BLACK
	pixels[10] = WHITE

	# Right Eye
	pixels[11] = PURPLE
	pixels[12] = PURPLE
	pixels[13] = PURPLE

	# Right Eyebrow
	pixels[14] = WHITE

	# Large Brow
	pixels[15] = BLACK
	pixels[16] = BLACK
	pixels[17] = BLACK
	pixels[18] = BLACK
	pixels[19] = BLACK
	pixels[20] = BLACK
	pixels[21] = BLACK
	pixels[22] = BLACK

	# Small Brow
	pixels[23] = BLACK
	pixels[24] = BLACK
	pixels[25] = BLACK
	pixels[26] = BLACK
	pixels[27] = BLACK
	pixels[28] = BLACK
	pixels[29] = BLACK

	# Forehead & Left Eyebrow
	pixels[30] = WHITE
	pixels[31] = BLACK
	pixels[32] = BLACK
	pixels[33] = BLACK
	pixels[34] = BLACK
	pixels[35] = BLACK
	pixels[36] = WHITE
	pixels[37] = BLACK
	pixels[38] = BLACK
	pixels[39] = WHITE

	# Left Eye
	pixels[40] = PURPLE
	pixels[41] = PURPLE
	pixels[42] = PURPLE

	# Left Cheek
	pixels[43] = WHITE
	pixels[44] = BLACK
	pixels[45] = BLACK
	pixels[46] = WHITE


	pixels.show()


def speak():
	color_fill(BLACK,.001) 


	# Mouth
	pixels[0] = RED
	pixels[1] = RED
	pixels[2] = RED
	pixels[3] = RED

	# Soul Patch
	pixels[4] = RED
	pixels[5] = RED
	pixels[6] = RED

	# Right Cheek
	pixels[7] = BLACK
	pixels[8] = BLACK
	pixels[9] = BLACK
	pixels[10] = BLACK

	# Right Eye
	pixels[11] = BLACK
	pixels[12] = BLACK
	pixels[13] = BLACK

	# Right Eyebrow
	pixels[14] = BLACK

	# Large Brow
	pixels[15] = RED
	pixels[16] = RED
	pixels[17] = RED
	pixels[18] = RED
	pixels[19] = RED
	pixels[20] = RED
	pixels[21] = RED
	pixels[22] = RED

	# Small Brow
	pixels[23] = RED
	pixels[24] = RED
	pixels[25] = RED
	pixels[26] = RED
	pixels[27] = RED
	pixels[28] = RED
	pixels[29] = RED

	# Forehead & Left Eyebrow
	pixels[30] = BLACK
	pixels[31] = BLACK
	pixels[32] = BLACK
	pixels[33] = BLACK
	pixels[34] = BLACK
	pixels[35] = BLACK
	pixels[36] = BLACK
	pixels[37] = BLACK
	pixels[38] = BLACK
	pixels[39] = BLACK

	# Left Eye
	pixels[40] = BLACK
	pixels[41] = BLACK
	pixels[42] = BLACK

	# Left Cheek
	pixels[43] = BLACK
	pixels[44] = BLACK
	pixels[45] = BLACK
	pixels[46] = BLACK


	pixels.show()	

# ************************************************************************************


color_fill(BLACK,.001) 
#show_all_pieces()


#stop_speaking()

'''
# What Adafruit CircuitPython 4.0.0-alpha looked like
for i in range(5):
	speak()
	time.sleep(0.2)
	stop_speaking()
	time.sleep(0.2)
	speak()
	time.sleep(0.2)
	stop_speaking()

	time.sleep(0.5)
'''


# What Adafruit CircuitPython 8.2.8 is capable of
for i in range(10):
	speak()
	#time.sleep(0.2)
	stop_speaking()
	#time.sleep(0.2)
	speak()
	#time.sleep(0.2)
	stop_speaking()

	time.sleep(0.1)

	
color_fill(BLACK,.001) 