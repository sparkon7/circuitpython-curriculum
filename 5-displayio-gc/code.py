'''
step 1: import the gc module for garbage collection features and
write a little helper to show our memory usage over time
'''
import gc

def update(msg):
	gc.collect()
	print(msg, " --> ", gc.mem_free())

update("import gc")

'''
step 2: now lets import the other necesary display libraries 
to see how much RAM they require
'''
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
update("import others")

'''
step 3: initialize the i2c and display bus 
'''
oled_reset = board.D9
displayio.release_displays()
i2c = board.I2C()  
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)
update("init i2c")

'''
step 4: initlaize the actual display
'''
w, h = 128, 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=w, height=h)
update("init display")

'''
step 5: initialize the visuals by assigning a blank screen to the device
'''
splash = displayio.Group()
display.show(splash)
update("assign blank splash")

'''
step 6: create a Bitmap that is the size of the display, and color
palette with two elements: white and black
'''
color_bitmap = displayio.Bitmap(w, h, 2)
color_palette = displayio.Palette(2)
color_palette[0] = 0xFFFFFF 
color_palette[1] = 0x000000
update("created bitmap")

'''
step 7: create and draw a TileGrid on the Bitmap
'''
bg_sprite = displayio.TileGrid(color_bitmap,
	pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
update("tilegrid")

'''
step 8: (try to) draw an inner rectangle to display text on
This is where memory allocation starts to fail! We do not have enough
RAM to store this large of a variable 
'''
# b = 5
# inner_bitmap = displayio.Bitmap(w-b*2, w-b*2, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000 # Black
# inner_sprite = displayio.TileGrid(inner_bitmap,
#                                   pixel_shader=inner_palette,
#                                   x=b, y=b)
# splash.append(inner_sprite)
# update("inner rectangle")

'''
step 8.b: draw some initial text on the screen - skip the memory-intensive background
'''
text_area = label.Label(terminalio.FONT, text="hello world!", color=0x000000, x=28, y=h//2-1)
splash.append(text_area)
update("text")

'''
step 9: set up our connection to the light sensor and display the initial value
'''
from analogio import AnalogIn
sens = AnalogIn(board.LIGHT)
update("light sensor")

'''
step 10: write some simple main function, to periodically poll the sensor and update the oled
'''
# def simple_main():
# 	from time import sleep
# 	while True:
# 		text_area.text = str(sens.value)
# 		sleep(0.5)

'''
step 11: write a more fun main function to also move the location of the text
'''
# def more_fun_main():
# 	from time import sleep
# 	from random import randrange
# 	while True:
# 		v = str(sens.value)
# 		text_area.text = v
# 		text_area.x = randrange(0,128-len(v))
# 		text_area.y = randrange(0,64)
# 		sleep(0.5)

'''
step 12: lets write a function to graph the light value over time
remember, the light sensor returns values in the range (0, 65000)
'''
def graph_main():
	from time import sleep
	text_area.text = ""
	for i in range(128):
		for j in range(64):
			color_bitmap[i,j] = 0
	x = 0
	while x < 128:
		val = sens.value
		y = int(64 * (1 - (val / 65000)))
		color_bitmap[x,y] = 1
		sleep(0.05)
		x += 1

while True:
	gc.collect()
	# simple_main()
	# more_fun_main()
	graph_main()