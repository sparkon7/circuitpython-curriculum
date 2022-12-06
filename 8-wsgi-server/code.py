'''Step 1: Import our libraries'''
import board
import busio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_esp32spi.adafruit_esp32spi_wsgiserver as server
from adafruit_wsgi.wsgi_app import WSGIApp
import json
from secrets import secrets

'''Step 2: Initialize our ESP32 WiFi chip. This requires 4 pins/connections:
    - SPI connection to transport data
    - CS (chip select) pin to tell ESP32 to wake up/be ready to receive/send data
    - "ready" pin to indicate when data is ready to be sent
    - "reset" pin to reset the ESP32 '''
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

'''Step 3: Initialize our WiFi manager, which is responsible for managing the
ESP32s WiFi connection. The `wifimanager.ESPSPI_WiFiManager` class constructor
accepts the following arguments (and more optional ones):
    - an `adafruit_esp32spi.ESP_SPIcontrol` object
    - `secrets` dictionary containing ssid and password
    - a `NeoPixel` status light
    - `debug`: an optional boolean. When set to `True`, the constructor will print
                information about the WiFi connection '''
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1) 
wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light, debug=True)
wifi.connect()
print("open this IP in your browser: ", esp.pretty_ip(esp.ip_address))

'''Step 4: Create our `WSGIApp` and `WSGIServer` to handle web requests'''
web_app = WSGIApp()
server.set_interface(esp)
wsgiServer = server.WSGIServer(80, application=web_app)

'''Step 4.a: Write a method `led_on` which sets the NeoPixel to a specific color'''
@web_app.route("/led_on")
def led_on(request): 
    status_light[0] = (100, 100, 255)
    return ("200 OK", [], "led on!")

'''Step 4.b: Write a method `led_off` which turns off the NeoPixel'''
@web_app.route("/led_off")
def led_off(request):  
    print("led off!")
    status_light[0] = (0, 0, 0)
    return ("200 OK", [], "led off!")

'''Step 5: Write a more complex method, `led_custom`, which accepts POST requests
and requires a body of data to be sent within the request. The request should include
the following data:
    "r": the "r" value for the NeoPixel RBG 
    "g": the "g" value for the NeoPixel RBG 
    "b": the "b" value for the NeoPixel RBG '''
@web_app.route("/led_custom", methods=["POST"])
def led_custom(request):
    data = json.load(request.body)
    for key in data.keys():
        data[key] = int(data[key])
    status_light[0] = (data['r'], data['g'], data['b'])
    return ("200 OK", [], "custom!")

'''Step 6: Write a method which handles errors, `led_custom_handle_err`'''
@web_app.route("/led_custom_handle_err", methods=["POST"])
def led_custom_handle_err(request):
    data = json.load(request.body)
    try:
        for key in data.keys():
            data[key] = int(data[key])
        status_light[0] = (data['r'], data['g'], data['b'])
        return ("200 OK", [], "custom!")
    except Exception as e:
        exc_type = type(e).__name__
        exc_msg = str(e)
        msg = exc_type + ": " + exc_msg
        return ("400 Bad Request", [], msg)

'''Step 7: Run the server, continually polling for requests and checking that
the WiFi connection is still active '''
wsgiServer.start()
while True:
    try:
        wsgiServer.update_poll()
    except (ValueError, RuntimeError) as e:
        print("Failed to update server, restarting ESP32\n", e)
        wifi.reset()
        continue
