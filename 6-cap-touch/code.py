'''Step 1: import our libraries'''
import time
import board
import neopixel
import touchio

'''Step 2: Create our neopixel strip object. Remember, the CPX has 10 lights'''
pix = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

'''Step 3: Declare a list containing `strings` naming the the touch-input
pins on our board, such as "A1". Also, declare a list containing `ints` 
defining the pixel associated with each touch pin.'''
pin_names = ["A1", "A2", "A3", "A4", "A5", "A6", "TX"]
pix_locs =  [6,     8,     8,    0,    1,   3,    3]


'''Step 4:
helper function to create a list of touchable pin objects from `pin_names`
Return:
	a list of `touchio.TouchIn` objects'''
def make_touchable():
	touchables = pin_names.copy()
	for i in range(len(pin_names)):
		pin = getattr(board, pin_names[i])
		touchables[i] = touchio.TouchIn(pin)
	return touchables

'''Step 5:
helper function to determine which of pins are being touched
Parameters:
	touches: a list of [touchio.TouchIn] objects representing our touch input pins
Return:
	a list of [True/False], where True means the pin is being pressed'''
def which_touched(touchables):
	touched = []
	for t in touchables:
		touched.append(t.value)
	return touched

'''Step 6
helper function to light up the neopixels we have associated with the 
touchable pins on our board
Parameters:
	touched: a list of [True/False] entries, True for pins currently being touched'''
def light_touched(touched):
	on_color = (0, 100, 0)
	off_color = (0, 0, 0)
	on = []
	for i, touched in enumerate(touched):
		loc = pix_locs[i]
		if touched:
			pix[loc] = on_color
			on.append(loc)
		elif loc not in on:
			pix[loc] = off_color
	pix.show()


'''Step 7
main logic to light up the associated neopixels when pins are touched'''
def main_display_touched():
	touchable = make_touchable()
	while True:
		vals = which_touched(touchable)
		light_touched(vals)
		time.sleep(0.1)

''' Step 8: Call our `main()` function indefinitely'''
main_display_touched()
