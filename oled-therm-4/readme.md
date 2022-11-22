# OLED! Thermometer! Your second CircuitPython Project
In this fun project, we will see a few new concepts
1. using an `I2C` connection to communicate with external devices (an OLED)
2. displaying information on an OLED screen
3. using the builtin sensors on your CircuitPlayground Express (this exercise will use the thermistor)

# Project Outline
By the end of this project, you will have a small device that periodically displays the temperature (in Fahrenheit) on the connected OLED screen.
Here is a rough project outline
- Import the necessary libraries to drive the thermistor and OLED display
- Initialize an I2C connection and I2C display bus (more on these later) for the board to communicate with the OLED
- Initialize a thermistor driver to communcate with the onboard sensor
- Write a simple function named `get_tempF()` that uses our thermistor driver instance to read and return the temperature in Fahrenheit
- Write a `main` function that uses `get_tempF()` to display a friendly message to the user telling them the current temperature.
- To finalize our CircuitPython program, per usual, call your `main()` function indefintely within a `while True` statement. Use the `time.sleep` function to pause for a short period of time between readings. 

# Displaying data on the OLED
Because the CircuitPlayground Express is resource-constrained, it does not have enough onboard memory to use the official animation and display libraries provided by Adafruit.
Luckily, that will not stop us from being able to display data.
Because our board is connected to the OLED via an I2C serial connection, any serial output from our program will be captured by this connection and displayed on the screen.
This means we can simply use the `print()` function to output data.

# What is I2C?
I2C (Inter-Integrated Circuit) communcation is a "language" that computers/devices speak to each other. 
Just like humans need to communicate using the same language, computers do too.
There are many different pros and cons to each language/protocol, but I2C is popular because...
1. Only requires 1 or 2 communication wires
2. "shared bus" protocol - can communicate with 100+ devices simultaneously
3. Implemented on lots of devices
### So what is an I2C "address"?
Each I2C device (an OLED, a sensor, etc) has a unique I2C address in the range of 0-127. 
This allows our board to communicate with multiple (up to 127) devices at a time.
When creating an I2C bus instance, we need to specify the I2C address so our data is sent to and read from the proper data.
The preassigned address for our 128x64 monochrome OLED in `0x3d`, which is hexadecimal for 61.
### But what about an I2C "bus"?
I2C is simply the protocol for how the board and device understand each others messages.
A "bus" is the tool that transports data to and from the microcontroller and OLED screen.
So in order to create an instance of our OLED screen, we need both an I2C instance and an I2C bus instance. 

# Using Builtin Sensors
Generally, external devices will be connected with multiple wires, and you will have to keep track of these connections in order to use the device.
For example, if we have a wired sensor with input connected to boards `D9` and output to `D10`, we will need to reference the pins as `board.D9` and `board.D10` in the proper places in our CircuitPython code. 
But luckily, we can directly reference the builtin sensors by name.
For example, to reference the data pins of the speaker, we can simply state `board.SPEAKER`. 
And similarly, to reference the data pins of the thermometer, we can use `board.THERMISTOR`.
