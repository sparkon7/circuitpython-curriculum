# OLED! Thermomter! Your second CircuitPython Project
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

# What is I2C?
I2C (Inter-Integrated Circuit) communcation is a "language" that computers/devices speak to each other. 
Just like humans need to communicate using the same language, computers do too.
There are many different pros and cons to each language/protocol, but I2C is popular because...
1. Only requires 1 or 2 communication wires
2. "shared bus" protocol - can communicate with 100+ devices simultaneously
3. Implemented on lots of devices
### But what about an I2C "bus"?
I2C is simply the protocol for how the board and device understand each others messages.
A "bus" is the tool that transports data to and from the microcontroller and OLED screen.
So in order to create an instance of our OLED screen, we need both an I2C instance and an I2C bus instance. 
