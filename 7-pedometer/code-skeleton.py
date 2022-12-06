'''Step 1: Import our required external libraries'''
import time
import board
import adafruit_lis3dh
from busio import I2C
from digitalio import DigitalInOut
import displayio
import adafruit_displayio_ssd1306

'''Step 2: Initialize our I2C connection and physical display
Return:
    `adafruit_displayio_ssd1306.SSD1306` object'''
def create_display():
    displayio.release_displays()
    i2c_address = 0x3d
    ...  # finish the initialization here

'''Step 3: Initialize a connection to our onboard accelerometer
Return:
    `adafruit_lis3dh.LIS3DH_I2C` object'''
def create_accelerometer():
    i2c_address = 0x19
    ...  # finish the initialization here

'''Step 4: Compute and return a scaled reading of the current x,y,z acceleration
Parameters:
    `sensor`: `adafruit_lis3dh.LIS3DH_I2C` object representing our onboard accelerometer
Return:
    `[float]` list containing scaled x,y,z accleration values'''
def scaled_reading(sensor):
    grav = adafruit_lis3dh.STANDARD_GRAVITY
    scaled_vals = []
    # take a reading from the sensor and scale the results by `grav`
    ...
    return scaled_vals

'''Step 5: Compute and return the current acceleration magnitude. 
Parameters:
    `scaled_reading`: `[float]` list containing scaled x,y,z acceleration values
Return:
    `float` value of current acceleration magnitude'''
def compute_magnitude(scaled_reading):
    ...  # finish this function

'''Step 6: Create a simple threshold pedometer. This pedometer counts a "step" when
it sees an acceleration magnitude of greater than the given `threshold`. Maintain a 
counter for steps, and display this value on the display using a `print` statement.
Parameters:
    `threshold`: the acceleration magnitude which defines a step'''
def simple_threshold_pedometer(threshold):
    ... # call your `create_` functions to build your display and sensor
    count = 0
    while True:
        ... # take a reading, compute the magnitude, and (possibly) update your steps
        print("\n", count, "\n")
        time.sleep(0.05)

simple_threshold_pedometer(3.5)
    
