# Wearable Pedometer! Count your steps
In this project, we are going to use our onboard OLED and acceleration sensor to count and display the number of steps we've taken.
This project is going to cover the use of I2C to connect to devices, and how to read the builtin acceleration sensor. 
Using the acceleration sensor, we can get a reading of how much the CPX is moving.
We will use this reading to determine when a step has taken place. 
A step will be defined as a movement with an acceleration magnitude greater than some threshold (in my tests, a threshold of 3.5 m/s^s was accurate).

# Project Outline
1. As always, import our libraries. The new one this project is `adafruit_lis3dh`, which allows us control over the onboard `LIS3DH` accelerometer.
2. Write a function, `create_display()` to initialize our physical dispay. Remember, the display relies on an `I2C` connection to our CPX. Once you have constructed the `displayio.I2CDisplay` object, you can use that to create our `adafruit_displayio_ssd1306.SSD1306` object to control the physical display.
3. Write the `create_accelerometer()` function, which initializes an I2C-connected acceleromter. We first need to create an I2C connection using the `busio.I2C` module. This connection will use the pins `board.ACCELEROMETER_SCL` and `board.ACCELEROMETER_SDA`, and have the address `0x19`. Using this connection, you can create your accelerometer with  

    ```sensor = adafruit_lis3dh.LIS3DH_I2C(connection, address=0x19)```
4. Implement the function `scaled_reading(sensor)`, which takes as input a connection to our `LIS3DH` accelerometer, and computes a gravity-scaled reading of the acceleration in the x, y, and z directions. To "gravity-scale" a reading, simply divide it by `adafruit_lis3dh.STANDARD_GRAVITY`. This function should return a list of the scaled `[x, y, z]` readings.
5. Write `compute_magnitude(scaled_reading)`, which takes as input the list of scaled `[x,y,z]` acceleration readings, and computes the acceleration magnitude. Remember, the magnitude is simply the sum of the squared values. Return the magnitude as a `float`.
6. Write a function to count and display the number of steps the wearer has taken so far, `simple_threshold_pedometer(threshold)`. The first steps are to initialize the display and accelerometer, so we can count and display our steps. Next, indefintely (within a `while True` block) take a scaled reading of the acceleration and then compute the magnitude. If the magnitude is greater than the `threshold` parameter, update the count of steps on the screen.

# Accelerometer
Our CPX has a builtin `LIS3DH` accelerometer, which can measure the rate of change in speed (in m/s^2).
We communicate with our accelerometer using an I2C connection, which we have to manually create (its simple, dont worry).
The `LIS3DH` is "triple-axis", which means it can measure acceleration in the x, y, and z directions. 
To better understand our readings, we need to "scale" them by the standard gravity value of Earth (because, science). 
This simply means dividing each x, y, and z value by `adafruit_lis3dh.STANDARD_GRAVITY`, which is a `float` representing Earth's gravity. 

# I2C Refresher
So, we've seen `I2C` plenty of times now, but it's always good to refresh.
`I2C` is a language that computers/devices use to communcate with each other.
Both the OLED and the accelerometer will communicate with our CPX using I2C.
Multiple I2C connections on the same board are differentiated by their address. 
The address of our OLED is `0x3d`, and the address of our accelerometer is `0x19`. 
Our OLED will use the builtin `board.I2C()` singleton for its connection.
That means that for the accelerometer, we will need to create another I2C instance using unused pins.
To do this, use the `I2C` object from `busio` and initialize it with the proper pins.
The CPX has builtin pins reserved for communication with the accelerometer you can use to create the connection.

```accel_i2c = I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)```.

# Being memory-conscious with the OLED
To avoid crashing our board with memory errors, we are going to simply `print()` our output, instead of creating `BitMaps` and `Tilegrids` like project 5. Because the OLED is connected via I2C, it captures all serial output, thus displaying the content we `print()`.