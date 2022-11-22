# LED Patterns! Your first CircuitPython Project
Welcome to your first CircuitPython project! 
In this project, we will use the builtin NeoPixels on your CircuitPlayground Express boards to display a pretty, custom pattern.
This project will introduce us to
1. using the `board` module to communicate with the pins of the board
2. using those pins to control external devices with the `neopixel` module
3. writing and uploading code for microcontrollers

# Project outline
The goal of this project is to display a custom pattern on your device. The outline of this project is...
1. Import the necessary libraries. For this, we only need `board` and `neopixel`
2. Create an instance of the NeoPixel driver to control the color and brightness of our lights. The constructor has 2 required arguments, and 2 optional keyword arguments which are very common.
	- pin: the `board.pin` constant representing the pin being used to communicate with the pixels
	- count: the number of pixels on the NeoPixel strip. Our board has 10.
	- brightness: the brightness value (between 0 and 1) of the LEDs. 1.0 is **very** bright, usually stick to 0.1. 
	- auto_write: whether or not the LED values should change automatically. If this value is `False`, we need to specify in our code when the changes take effect.
3. Lets write a helper method, `clear_pixels()`,  to set all of the pixel values to blank/off, which will be represented by the (R,G,B) triplet (0,0,0). We will call this method first to clear the stage for our display.
4. Lets write another helper method, `set_pixel_color`, which takes two arguments:
	- pixel: the index of the NeoPixel to change (between 0 and 9)
	- value: the (R,G,B) triplet color to set this pixel to
	
	to change the value of a pixel, you can simply index into the `pixels` object and assign the value as if you are changing an item in a list. After changing the value, print a short message describing the change, and call the `pixels.show()` method to display the changes. 
4. Now for the fun part. Using the two helper methods we created, `clear_pixels` and `set_pixel_color`, write another function `my_fun_pattern` to display your own fun pattern!
5. End your program by calling `my_fun_pattern()` indefinitely! Hint: use a `while` statement.
