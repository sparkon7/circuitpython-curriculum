# Garbage Collection? DisplayIO! Writing a memory-heavy project on a memory-constrained device
In this project, we're going to upgrade our knOwLEDge and work with Adafruits `displayio` library for formatting output to our OLED, and the `gc` library to manage memory.
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
While developing this functionality, we will work in a very step-by-step fashion, using the `gc` module to watch our memory usage and free any unused memory.
Just a note, this project is broken into more, **smaller** parts to ensure we check our memory consumption.
1. Import the `gc` module and oled modules, and write a little helper function to call the `collect()` function and print the current amount of free memory. We will use this to observe our usage over a serial console
2. Initialize the `I2C` connections to the OLED, and the then the physical display itself. 
3. This is where we start with `displayio`. We create the `Group` object which will serve as the container for all other visuals (text, colors, etc). How does this impact the memory?
4. The next `displayio` step is creating a `Bitmap` object and its corresponding color `Palette`. A `Bitmap` is a mapping of location to color, and is represented as a 2D list with a limited number of possible colors. Our `Bitmap` is 128 pixels tall, 64 pixels wide, and will have 2 possible colors: white and black. `append` this `Bitmap` to the `Group` object from step 5.
5. There's one more `displayio` object we need to deal with: a `TileGrid`. A `TileGrid` sits on top of a `Bitmap` and allows you to make changes to the display without changing the source `Bitmap`. It is a bit overkill for our use case today but maybe you can play around with its features afterwards. For this step, we simply create a `TileGrid` which sources from our initial, blank `Bitmap` and black & white `Palette` from step 6.
6. Add another bitmap to our display, a smaller black rectangle to serve as a frame for text we will later display. Oh no! We don't have enough memory... So instead, let's just display the text using a `Label` object from the `adafruit_display_text` library. A `Label` object has an associated font, which we will take from `terminalio`, text, color, and an x and y coordinate. Make sure to append this object to the `Group`. 
7. It seems like we have around 1000 bytes left in memory. This is probably enough to do some simple plotting of the light sensor value. First off, lets initialize our light sensor and display the initial reading as the text in our `Label`.
8. Write a `poll()` function which periodically polls the light sensor, and displays the value on the OLED by changing the `Label.text` property. Import whatever extra functionality you need within the function, so that if we use a different function later on, the memory is not wasted.
9. It seems like we have some extra memory, let's use it! Write a `moving_poll()` function, which is similar to the `poll()`, but also changes the `x` and `y` properties of the `Label` so that the reading moves across the display. Hint: use a function from the `random` library
10. Now, enough with just displaying the value in text on the screen. How informative is that, really? Let's make a simple plotter to make a moving graph of the value. More on this below...

Don't forget to call your desired `main` function within a `while True` block at the end of your program!

# Garbage Collection
The `garbage collector` is the software that Python and CircuitPython uses to manage its memory. When an object is stored in memory, such as when you type `x=5` , your computer takes that `5` and stores it at some memory address, such as `0x0AE43C`, and `gc` keeps a record that `x` points to the address `0x0AE43C`. That's helpful for you as a programmer because you can just refer to the data as `x` without needing to know/care about its address. 

Every once in a while, Python will execute an automatic "garbage collection" process, in which `gc` will sweep the memory, looking at every address and ensuring the associated variable is still being used by your program. If not, `gc` will remove the record of that variable, and then that address will be "freed" and available to use for another object. 

Bad things happen when you run out of RAM. Your board will crash in unrecoverable ways (meaning your program won't run and you'll need to reprogram it, no explosions), and sometimes the issue can be hard to solve. Often, your only option is to reduce the size of your program or use a microcontroller with more memory. 

Check out the helper function, `update()`. This simply calls `gc.collect()`, and then prints the amount of free memory remaining using `gc.mem_free()`. We call `collect()` to execute a garbage collection process which will clean up any unused memory we have created. Unused memory can be caused by large variables created in functions, or from importing heavy libraries. We're going to call `update()` after large operations to check our memory status. 

Some easy tips for managing memory are to call `gc.collect()` after a function which creates lots of variables has been created, or after large objects are done being used. Additionally, only import what you need from a library using the `from ... import ...` syntax.

# I2C and the Display Bus
Remember, I2C is a language that computers/devices use to communicate. We are using I2C to send data from the CPX to our OLED device. The CPX has builtin I2C, so we can simply access the connection using the provided `board.I2C()` object. The second step in establishing an I2C connection is creating the I2C "bus", which actually transports the data over the connection. Think of this as a little bus driver just going back and forth. Once we have the connection in the form of the `displayio.I2CDisplay` object, we can initialize our physical display from the `adafruit_displayio_ssd1306.SSD1306` object. 

# Groups, Bitmaps, TileGrids, and Labels
That's a lot. These are the building blocks of the graphics library, `displayio`. Adafruit will explain these much better than I will. [here are the official docs](https://learn.adafruit.com/circuitpython-display-support-using-displayio/library-overview)
### Updating Text
The text on our OLED is represented in our code by the `text_area` object. This object has 3 relevant properties, `text`, `x`, and `y`. As you can imagine, the `text` property is the string of text to display on the OLED, and `x` and `y` are the coordinates of where to place the first letter. To change the display, you can simply change the properties like `text_area.text = "some new words"`.
### Updating the Bitmap
Remember, the `Bitmap` object is a mapping of pixel --> color, and is represented as a 2D list, or matrix. The top left of the screen is at location (0,0), and can be accessed by `color_bitmap[0,0]`. The values in the Bitmap correspond to colors in our `Palette`, which is simply just a list of possible colors in the Bitmap. Our `Palette` has two entries, white and black, so the possible entries in our Bitmap are `0` for white and '1' for black. To set the top left pixel black, update the Bitmap like `color_bitmap[0,0] = 1`.

# Using the Light Sensor
The CPX has a builtin light sensor, which is simple to use but covers a topic we haven't yet seen: analog input. The thermistor we used in project 4 was read on a digital pin. The difference between the two is that analog pins can be written/read continuously at any voltage. Think of analog pins as dimmer switches on lights, and digital pins as simple on/off switches. With the light sensor on a digital pin, we can take a continous reading of the light value in our surroundings. To use this, we need to import some functionality from the `analogio` library, but to be memory-cautious we are going to only import the `AnalogIn` object. 

The board has a builtin connection to the light sensor which we can access through `board.LIGHT`. The full code we need to create the sensor object is
```python
from analogio import AnalogIn
sens = AnalogIn(board.LIGHT)
```
You can read the value by accessing the property `sens.value`. The lowest, darkest reading is 0, and the highest, brightest reading is around 65k.

# Making a plotter
We are going to make a plotter that shows a moving graph of the light sensor reading on the device. The first step here is to remove the text from the screen. We do that by setting the `text` property of our `text_area` object to an empty string. 

Next, we need to set the entire screen to white. We do this using two for loops to sweep over all pixels in the display (remember, 128x64), and setting the values to white, which is the first element of our `Palette` (so value `0`). 

Now for plotting the values. Our x-axis will represent time, and our y-axis will be a scaled reading of the light sensor. To plot a point for the `10`th timestep, take a reading from the sensor, and scale it as such.
```python
raw_value = sens.value
y = 64 * (1 - (val / 65000))
y = int(y)
```
The first step here is reading the raw value, which lies in the range `(0,65000)`. Lets bbreak down the next step, which squishes this number in the range `(0,64)` to fit on our device. We first divide our reading by the max value, which gives us a percentage of how strong our light is. If the light is very strong, this will be closer to `1.0`. Next, we inverse this reading by subtracting it from 1. This is because the top of our plot is at coordinates `0`, so we want high reading values to actually give low numbers. Finally, we multiply this number by 64 to get a score in our range. Before plotting this value, we need to convert it to an `int`, so the `Bitmap` can use it to index the `Palette`. 
