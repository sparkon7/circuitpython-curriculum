# Introduction to CircuitPython!
CircuitPython is a version of Python that is designed to run on microcontroller boards, such as the CircuitPlayground Express.
CircuitPython provides a high-level, user-friendly interface for developers like yourself to write code for boards and hardware add-ons like sensors and cameras.

# Simple Anatomy of a CircuitPython Microcontroller
For the first projects we do, we will use the CircuitPlayground Express board, from Adafruit.
This little board packs a punch, with 
1) Pins/Jumper Connections: A pin can read or send small electrical currents, which can be used to interact with outside devices.
2) JST Battery Connection: The small black block on the bottom of the device is for powering it with a battery pack.
3) MicroUSB plug: This can be used to power the device, and/or read/write data to another device.
4) Lights!
5) Input/Output devices builtin! This board includes a microphone, two buttons, a switch, and speaker.
5) Sensors! Temperature, motion, and sound speakers to read its surroundings.
6) Infrared Receiver and Transmitter for sending IR messages and communicating between devices.

# Anatomy of a CircuitPython Project
A CircuitPython project has a simple file structure
1) `boot.py`: this file is executed when CircuitPython starts up. It is commonly used to change system settings, such as storage rules, or create any files/folders your project needs.
2) `code.py`: this is the main logic of your project, which CircuitPython will execute after it boots up
3) `lib/`: this folder contains the external CircuitPython libraries your project needs, in `.mpy` format. 

# Writing CircuitPython Code
There are two main ways to execute CircuitPython on a microcontroller
### Via the REPL
The REPL is Python's read-evaluate-print-loop, which allows you to enter individual lines of code and have them run immediately. 
To access the REPL, you must first make a serial/usb connection to the device.
Once you have plugged in your device, you can use a serial communcation tool such as `tio`, or the serial extension on VSCode, to access the device's serial console. 
From there, you can press any button to access the REPL.
You should see a line of text like
```
Adafruit CircuitPython 8.0.0-beta.4 on 2022-10-30; Adafruit CircuitPlayground Express with displayio with samd21g18
>>> 
```
From there, you can enter code and see the results.
```
Adafruit CircuitPython 8.0.0-beta.4 on 2022-10-30; Adafruit CircuitPlayground Express with displayio with samd21g18
>>> print("hello world!")
hello world!
```
### Loading `.py` files onto the device
When you plug a CircuitPython device into your computer via USB, it shows up as a USB device with the name `CIRCUITPY`.
From there, you can use your favorite IDE to edit the `boot.py` and `code.py` files, as well as copy the `.mpy` folders into the device's `lib/` directory 

# Memory on CircuitPython Devices
Computers have two different types of memory.
Nonvolatile, or "Flash" memory, retains its data even after power is turned off. This is used to store program files, such as your `code.py`, audio files, fonts, etc.
Volatile memory, or "RAM", is used to store all of the variables and data your code creates and needs. 
Microcontrollers are "memory-constrained" devices.
This means that as a programmer you need to be aware of how much memory your program needs and if your board can handle the task. 
Many of our projects will use the Adafruit CircuitPlayground Express. The CPX has
- 2 MB of Flash storage
- around 17k bytes of memory, which is about 250 lines of code 
### Do I have enough Flash?
To determine if your board has enough Flash memory to run your project, you can use your file explorer to determine the size of each file. Remember to include your `code.py`, `boot.py`, and any `.mpy`, font, or other files your program will rely on. 
### Do I have enough RAM?
Theres no good way to determine this before hand.
CircuitPython provides us with the `gc` library for functionality related to the garbage collector, which is the name of Python's memory manager. 
The `gc` library provides many functionalities, but for now we are most interested in
- `gc.collect()`: This function will instruct the garbage collector to free up any unused memory at this point in the program. It is helpful to call this at certain points in your program.
- `gc.mem_free()`: This function will return the amount (in Bytes) of free and usable memory.
- `gc.mem_alloc()`: This function will return the amount (in Bytes) of allocated (currently being used) memory.
