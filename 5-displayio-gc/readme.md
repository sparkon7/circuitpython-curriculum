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
1. Import the `gc` module and write a little helper function to call the `collect()` function and print the current amount of free memory. We will use this to observe our usage over a serial console
2. Import the rest of the requires modules for the base OLED and board functionality. Use the `update()` function to observe how the amount of free memory has decreased.
3. As we always have to do with the OLED, initialize the i2c and display bus. Out of curiousity and caution, we'll check the memory again.
4. Initialize our reference to the physical OLED display, using the `display_bus` object. Again, check the memory. How much can we safely do with this amount left?
5. This is where we start with `displayio`. We create the `Group` object which will serve as the container for all other visuals (text, colors, etc). How does this impact the memory?
6. The next `displayio` step is creating a `Bitmap` object and its corresponding color `Palette`. A `Bitmap` is a mapping of location to color, and is represented as a 2D list with a limited number of possible colors. Our `Bitmap` is 128 pixels tall, 64 pixels wide, and will have 2 possible colors: white and black. `append` this `Bitmap` to the `Group` object from step 5.
7. There's one more `displayio` object we need to deal with: a `TileGrid`. A `TileGrid` sits on top of a `Bitmap` and allows you to make changes to the display without changing the source `Bitmap`. It is a bit overkill for our use case today but maybe you can play around with its features afterwards. For this step, we simply create a `TileGrid` which sources from our initial, blank `Bitmap` and black & white `Palette` from step 6.
8. Add another bitmap to our display, a smaller black rectangle to serve as a frame for text we will later display. Oh no! We don't have enough memory... So instead, let's just display the text using a `Label` object from the `adafruit_display_text` library. A `Label` object has an associated font, which we will take from `terminalio`, text, color, and an x and y coordinate. Make sure to append this object to the `Group`. 
9. It seems like we have around 1000 bytes left in memory. This is probably enough to do some simple plotting of the light sensor value. First off, lets initialize our light sensor and display the initial reading as the text in our `Label`.
10. Write a `simple_main()` function which periodically polls the light sensor, and displays the value on the OLED by changing the `Label.text` property.
11. It seems like we have some extra memory, let's use it! Write a `more_fun_main()` function, which is similar to the `simple_main()`, but also changes the `x` and `y` properties of the `Label` so that the reading moves across the display. Hint: use a function from the `random` library
12. Now, enough with just displaying the value in text on the screen. How informative is that, really? Let's make a simple plotter to make a moving graph of the value. 