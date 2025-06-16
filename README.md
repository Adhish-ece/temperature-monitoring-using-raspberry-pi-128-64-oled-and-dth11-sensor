Raspberry Pi DHT11 Temperature Display on OLED
This project uses a Raspberry Pi to read temperature data from a DHT11 sensor and display it on an SSD1306 OLED screen.

Features
Reads temperature from a DHT11 sensor.
Displays the temperature in Celsius on a 128x64 SSD1306 OLED display.
Refreshes the display every 5 seconds.
Handles sensor errors gracefully.
Hardware Requirements
Raspberry Pi (any model with GPIO pins)
DHT11 Temperature and Humidity Sensor
SSD1306 OLED Display (128x64, I2C)
Jumper Wires
Breadboard (optional)
Software Requirements
Raspberry Pi OS (or any Debian-based Linux distribution for Raspberry Pi)
Python 3
Adafruit_DHT Python library
Adafruit-Blinka (for CircuitPython compatibility)
adafruit-circuitpython-ssd1306 Python library
Pillow (PIL) Python library
