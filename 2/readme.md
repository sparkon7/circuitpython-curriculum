# Introduction to CircuitPython!
CircuitPython is a version of Python that is designed to run on microcontroller boards, such as the CircuitPlayground Express.
CircuitPython provides a high-level, user-friendly interface for developers like yourself to write code for boards and hardware add-ons like sensors and cameras.

# Anatomy of a CircuitPython project
A CircuitPython project has a simple file structure
1) ```pythonboot.py````: this file is executed when CircuitPython starts up. It is commonly used to change system settings, such as storage rules, or create any files/folders your project needs.
2) ```pythoncode.py```: this is the main logic of your project, which CircuitPython will execute after it boots up
3) ```pythonlib/```: this folder contains the external CircuitPython libraries in `.mpy` format. 
When you 
