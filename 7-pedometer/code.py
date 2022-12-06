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
    i2c = board.I2C()
    bus = displayio.I2CDisplay(i2c, device_address=i2c_address, reset=board.D9)
    display = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)
    return display

'''Step 3: Initialize a connection to our onboard accelerometer
Return:
    `adafruit_lis3dh.LIS3DH_I2C` object'''
def create_accelerometer():
    i2c_address = 0x19
    i2c = I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    accel = adafruit_lis3dh.LIS3DH_I2C(i2c, address=i2c_address)
    return accel

'''Step 4: Compute and return a scaled reading of the current x,y,z acceleration
Parameters:
    `sensor`: `adafruit_lis3dh.LIS3DH_I2C` object representing our onboard accelerometer
Return:
    `[float]` list containing scaled x,y,z accleration values'''
def scaled_reading(sensor):
    grav = adafruit_lis3dh.STANDARD_GRAVITY
    scaled_vals = []
    raw_vals = sensor.acceleration
    for rv in raw_vals:
        scaled = rv / grav
        scaled_vals.append(scaled)
    return scaled_vals

'''Step 5: Compute and return the current acceleration magnitude. 
Parameters:
    `scaled_reading`: `[float]` list containing scaled x,y,z acceleration values
Return:
    `float` value of current acceleration magnitude'''
def compute_magnitude(scaled_reading):
    mag = 0
    for sr in scaled_reading:
        mag += sr ** 2
    return mag

'''Step 6: Create a simple threshold pedometer. This pedometer counts a "step" when
it sees an acceleration magnitude of greater than the given `threshold`. Maintain a 
counter for steps, and display this value on the display using a `print` statement.
Parameters:
    `threshold`: the acceleration magnitude (m/s^2) which defines a step'''
def simple_threshold_pedometer(threshold):
    display = create_display()
    accel = create_accelerometer()
    count = 0
    while True:
        read = scaled_reading(accel)
        mag = compute_magnitude(read)
        if mag > threshold:
            count += 1
        print("\n", count, "\n")
        time.sleep(0.05)

simple_threshold_pedometer(3.5)
    
