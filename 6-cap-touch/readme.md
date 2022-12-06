# Holding hands with your CPX! Capacitive touch
Notice those shiny gold tabs around the edge of your CPX?
Instead of using pins for making connections to external devices, the CPX uses "pads".
These can be connected to wires via the use of jumper/alligator clips, or wrapping exposed wire through the hole. 
Alternatively, some of them can also sense touch!
The following pads on the board support "capacitive" touch.
```A1, A2, A3, A4, A5, A6, TX```.

In this project, we are going to control the `neopixel` lights on our board using these cap touch connections. When a connection is touched, the nearest light will be illuminated. 

# Project Outline
1. As always, we need to import our necessary libraries. This time, we only need the following:
    - `time`: for controlling the execution of our program
    - `board`: for accessing builtins such as pins and I2C
    - `neopixel`: to control the lights on our board
    - `touchio`: for reading the capacitive touch inputs
2. Initialize a `NeoPixel` object to control the strip of lights on the board
3. Declare two lists, `pin_names` containing the `string` human-friendly names of touch pins, and `pix_locs` containing the indexes/locations of the light associated with the pin. For example, 
    ```
    pin_names = ["A2", "A4"]
    pix_locs =  [0,    6]
    ```
    Means that we have two cap-touch pins, `A2` and `A4`, where `A2` is closest to neopixel `0` and `A4` is closest to neopixel `6`. The `pin_names` list will be used to create a list of `touchio` objects

4. Write a helper function named `make_touchable()`, which uses the `pin_names` list to create a list of `touchio.TouchIn` objects. This will require the use of `getattr(obj, attr)`. More on this below. The output of this function should be a list of `touchio.TouchIn` objects for each pin in `pin_names`.
5. Write the function `which_touched(touchables)`, where the argument `touchables` is the list of touch pins created in step 4. This function should return a list of booleans representing which pins are currently being touched.
6. Write another function, `light_touched(touched)`, to illuminate the neopixels whose associated cap touch pins are being touched. This function should take one argument, a list of booleans representing which pins are being touched (from step 5). You'll need to write a `for` loop for iterate through the `touched` list. If the value is `True`, illuminate the corresponding pixel. 
7. Write a function, `main_display_touched()` to use the functions we made in steps 4, 5, and 6 to create our `touchio` input objects, determine which are currently being touched, and illuminate the corresponding lights. Use a `while True` statement and a call to `time.sleep()` to make sure the program runs indefintely, pausing shortly each iteration. 
8. Easy step - just call your `main` function

# `getattr(obj, attr)`: dynamically accessing attributes and creating objects
In our project, we need to create a list of `touchio.TouchIn` objects to represent the pins being pressed. 
Instead of having to type a long list like `[touchio.TouchIn(board.A1), touchio.TouchIn(board.A2), ...]`, we'll use `getattr()`.
The builtin function `getattr(obj, attr)` returns the specified attribute from the given object.
Check out this example...
```python
var1 = getattr(board, "A1")
var2 = board.A1
var1 == var2  # -> True
```
This may seem strange, but it is very helpful in situations when we don't know exactly what attribute we want from the class.
For example, what if the pin we need to access is not known to our program? What if the user wrote the pin in a file, or the pin changes. 
```python
pin_name = get_pin()
print(pin_name)         # -> "A6"
# pin = board.pin_name  # ERROR! This does not work, no attribute `pin_name`
pin = getattr(board, pin)
print(pin)              # -> board.A6
```
In our case, `getattr` is useful because we want to easily change the list of pins without having to type `board` or `touchio.TouchIn` many times. 


# Using the Cap Touch Inputs
Using the touch input pads on our CPX is super easy. 
These touch pads have two possible values: `True`/high, when the pad is being touched, and `False`/low otherwise. 
To create a touch pad object in CircuitPython, you need the `board` and `touchio` modules. 
For example, defining a touch pad input on pin `A4` would look like:
```python
import board
import touchio

a4_pin = board.A4
a4_touch = touchio.TouchIn(a4_pin)
```
You can access the `value` property of the `TouchIn` object to see if it is being pressed.
```python
if a4_touch.value:
    print("I'm being touched!")
else:
    print("I am not being touched.")
```

# Controlling NeoPixels
To create a strip of neopixels, use the `neopixel.NeoPixel` class.
The `__init__` function takes two required arguments, the `pin` controlling the pixels, and the number of pixels in the strip. The control pin is builtin and defined as `board.NEOPIXEL`. Our CPX has 10 lights.

There are also some optional, keyword arguments to remember.
`brightness` controls the brightness level of the pixels, from `0` to `1.0`. 
A value of `0.1` is usually enough for testing, the lights are very bright.
The keyword argument `auto_write` is a boolean (`True` or `False`) that determines if the neopixels should automatically change their appearance, or if they should wait until we tell them. 
Set it to `False` for better control of the pixels appearance.

Creating a strip of pixels looks like
```python
import board
import neopixel

pix = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)
```

You can update the color of a single pixel by indexing into the `pix` object and assiging an RGB value to it, like...
```python
green = (0, 100, 0)
pix[0] = green
pix.show()
```
Make sure to call `pix.show()` when you are done making changes.