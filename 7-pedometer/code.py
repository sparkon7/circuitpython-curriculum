import time
import board
import adafruit_lis3dh
from busio import I2C
from digitalio import DigitalInOut
import displayio
import adafruit_displayio_ssd1306

def create_display():
    displayio.release_displays()
    i2c = board.I2C()
    bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.D9)
    display = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)
    return display

def create_accelerometer():
    i2c = I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    int1 = DigitalInOut(board.ACCELEROMETER_INTERRUPT)  
    accel = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
    return accel

def scaled_reading(sensor):
    grav = adafruit_lis3dh.STANDARD_GRAVITY
    raw_vals = sensor.acceleration
    scaled_vals = []
    for rv in raw_vals:
        scaled = rv / grav
        scaled_vals.append(scaled)
    return scaled_vals

def compute_magnitude(scaled_reading):
    mag = 0
    for sr in scaled_reading:
        mag += sr ** 2
    return mag

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

main()

    
