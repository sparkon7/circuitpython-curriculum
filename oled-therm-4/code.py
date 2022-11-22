'''
step 1: import the required modules
	`board`: create references to pins on the board for connections
	`displayio`: helper functions to manage displays such as our OLED
	`adafruit_displayio_ssd1306`: the specific drivers for our 128x64 OLED
	`adafruit_thermistor`: temperature sensor driver
	`time`: timing related functions (such as sleep/pause)
'''
import board
import displayio
import adafruit_displayio_ssd1306
import adafruit_thermistor
import time

# call this at the start of your program to reinitialize displays
displayio.release_displays()

'''
step 2: initialize I2C connection and I2C bus to be used by the OLED
The display bus requires a reset pin to be defined
The I2CDisplay bus constructor requires 3 arguments in our case
	- the I2C connection instance
	- `device_address`: the unique I2C address of our OLED
	- `reset`: the reset pin our OLED is listening to
'''
oled_reset = board.D9
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

'''
step 3: use the display bus to initialize a driver for our OLED
the SSD1306 constructor takes 3 arguments in our case:
	- an instance of the display bus, whether I2C (our case) or SPI
	- `width`: the width in pixels of our screen
	- `height`: the height in pixels of our screen
'''
WIDTH = 128
HEIGHT = 64  
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

'''
step 4: create thermistor instance. The constructor takes 4 arguments
	- board pin being used to control thermistor
	- resistance, normal temp, normal resistance, b_coefficient (these are 
	  specific to your board/wiring. For the CPX, just use these values)
'''
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

'''
step 5: write a function that will use the thermistor to return the current
temperature value in Fahrenheit. This function will take no arguments
'''
def get_tempF():
	tempC = thermistor.temperature
	tempF = tempC * 9 / 5 + 32
	return tempF

'''
step 6: write the main logic of your program, where you display the temperature
reading on the OLED board. For now, we will use the `print()` function to output
to the screen. Show the user a friendly message telling them the temperature.
'''
def main():
	tempF = get_tempF()
	msg = "Temp: " + str(tempF)
	print(msg)

'''
step 7: Use a `while True` statement to indefintely display the temperature by 
calling your `main()` function, pausing for 0.1 seconds each iteration
'''
while True:
	main()
	time.sleep(0.1)
