'''
step 1: import libraries
	the `board` library contains variables to reference the pins and specific board
	the `neopixel` library allows us to control the LEDs on board
'''
import board
import neopixel


'''
step 2: create a neopixel instance for this board
the neopixel constructor has 2 required arguments and two optional arguments
	#1: the pin (from the `board` module) being used to drive the NeoPixels
	#2: the number of NeoPixels in the strip
	brightness: a fraction between 0 and 1, the brightness value of the LEDs
	auto_write: whether or not the NeoPixel should change color automatically
		when the value is changed. When `False`, we need to call an `update()` 
		method for the lights to change 
'''
num_pixels = 10
pixels = neopixel.NeoPixel(...)  # finish this line


'''
step 3: write a method to clear all neopixels by setting their color = (0,0,0)
'''
def clear_pixels():
	for n in range(num_pixels):
		pixels[n] = (0,0,0)
	pixels.show()


'''
step 4: write a method called `set_pixel_color`, which will update the color value
of a pixel, print a message, and display the change.
This method takes two arguments
	`pixel`: the NeoPixel in the strip to update. This value sho
	`color`: the color to set the pixel in (R,G,B) format
'''
def set_pixel_color(pixel, color):
	print(pixel, " = ", color)
	...  # start your work here


'''
step 5: write your own method `my_fun_pattern` that will use the `set_pixel_color` 
	method to display a fun pattern on the board!
'''
...  # write your method here


'''
step 6: include the final bit of code to run `my_fun_pattern()` when this script is executed
'''
if __name__ == "__main__":
	...
