'''Step 1: import our libraries'''
import ...  

'''Step 2: Create our neopixel strip object. Remember, the CPX has 10 lights'''
pix = neopixel.NeoPixel(...  # finish creating the pix

'''Step 3: Declare a list containing `strings` naming the the touch-input
pins on our board, such as "A1". Also, declare a list containing `ints` 
defining the pixel associated with each touch pin.'''
pin_names = ["A1", "A2", ...
pix_locs =  [6,     8,   ...


'''Step 4:
helper function to create a list of touchable pin objects from `pin_names`
Return:
	a list of `touchio.TouchIn` objects'''
def make_touchable():
	touchables = pin_names.copy()
	for i in range(len(pin_names)):
		pin = ...            # use `getattr` to get our pin object
		touchables[i] = ...  # initialize a `touchio.TouchIn` object
	return touchables

'''Step 5:
helper function to determine which of pins are being touched
Parameters:
	touches: a list of [touchio.TouchIn] objects representing our touch input pins
Return:
	a list of [True/False], where True means the pin is being pressed'''
def which_touched(touchables):
	touched = []
	# write a `for` loop to check the `value` of every cap touch pin
	...
	return touched

'''Step 6
helper function to light up the neopixels we have associated with the 
touchable pins on our board
Parameters:
	touched: a list of [True/False] entries, True for pins currently being touched'''
def light_touched(touched):
	on_color = (0, 100, 0)
	off_color = (0, 0, 0)
	# write a `for` loop to iterate through `touched`
	# if the pin is being touched, set its color to `on_color`
	# otherwise, set its color to `off_color`
	...
	pix.show()


'''Step 7
main logic to light up the associated neopixels when pins are touched'''
def main_display_touched():
	# finish your main function
	...

''' Step 8: Call our `main()` function indefinitely'''
main_display_touched()
