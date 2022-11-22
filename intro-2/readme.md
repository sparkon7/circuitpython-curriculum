# Introduction to CircuitPython!
CircuitPython is a version of Python that is designed to run on microcontroller boards, such as the CircuitPlayground Express.
CircuitPython provides a high-level, user-friendly interface for developers like yourself to write code for boards and hardware add-ons like sensors and cameras.

# Simple Anatomy of a CircuitPython Microcontroller
For the first projects we do, we will use the CircuitPlayground Express board, from Adafruit.
This little board packs a punch, with 
1) Pins/Jumper Connections: A pin can read or send small electrical currents, which can be used to interact with outside devices.
2) `stemma` Cable Connection: The small black block on the bottom of the board is for plug 'n play connection of certain compatible devices also made by Adafruit.
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

# How to write a CircuitPython Project
TODO: This depends on what OS and IDE the students use. 
