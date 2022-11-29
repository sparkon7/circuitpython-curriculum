# Garbage Collection? DisplayIO! Writing a memory-heavy project on a memory-constrained device
In this project, we're going to upgrade our knOwLEDge and work with Adafruits `displayio` library for formatting output to our OLED. 
Because the CPX isn't the beefiest board in terms of memory, and OLED programming can be memory-intensive, we need to be careful with our code.
As a refresher, there are two types of memory for two different purposes:
- Flash memory: This storage is "persistent" across reboots, meaning it stays on the board when the power is off. This is how your `code.py` file (and others) are stored
- Random Access Memory (RAM): This is for the data your program creates and uses while it is running. 
To be cautious with you Flash consumption, minimize the amount of external libraries you rely on (`.mpy` files and `import` statements) and the actual size of your program files. 
To watch your RAM consumption, we rely on the `gc` library from Adafruit. `gc` stands for `garbage collector` which is Python's memory management software. 

# Project Outline
As a CircuitPython programmer, you do not have to manage your own memory. This means you don't have to ask for more memory or clear the memory you're done using.
But sometimes you want to, or at least you want to know how much is left before you run out and crash the board. 
This is especially true when working with the OLED on the CPX.
By the end of this project your device will be periodically reading its light sensor and displaying the value in various fun ways.