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
