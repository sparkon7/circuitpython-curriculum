import time
import board
import touchio
import neopixel

# list of human-friendly names of touch-input pins
pin_names = ["A1", "A2", "A3", "A4", "A5", "A6", "TX"]
# location of corresponding neopixel for each pin
pix_locs =  [6,     8,     8,    0,    1,   3,    3]

# create our pixel strip object
pix = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

'''helper function to create a list of touchable pin objects from `pin_names`
Returns a list of `touchio.TouchIn` objects'''
def make_touchable():
	touchables = pin_names.copy()
	for i in range(len(pin_names)):
		p = pin_names[i]
		p = getattr(board, p)
		p = touchio.TouchIn(p)
		touchables[i] = p
	return touchables

'''helper function to determine which of pins are being touched
Parameters:
	touches: a list of [touchio.TouchIn] objects representing our touch input pins
Returns a list of [True/False], where True means the pin is being pressed'''
def which_touched(touches):
	touched = []
	for t in touches:
		touched.append(t.value)
	return touched

'''helper function to light up the neopixels we have associated with the 
touchable pins on our board
Parameters:
	touched: a list of [True/False] entries, True for pins currently being touched'''
def light_touched(touched):
	on = []
	for i, t in enumerate(touched):
		loc = pix_locs[i]
		if t:
			pix[loc] = (0, 100, 0)
			on.append(loc)
		elif loc not in on:
			pix[loc] = (0, 0, 0)
	pix.show()


'''main logic to light up the associated neopixels when pins are touched'''
def main_display_touched():
	touchable = make_touchable()
	while True:
		vals = which_touched(touchable)
		print(vals)
		light_touched(vals)
		time.sleep(0.1)

main_display_touched()
