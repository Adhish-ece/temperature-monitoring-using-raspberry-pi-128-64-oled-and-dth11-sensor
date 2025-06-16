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

Installation
1. Enable I2C
First, ensure that I2C is enabled on your Raspberry Pi. You can do this using raspi-config:

sudo raspi-config

Navigate to Interface Options > I2C and enable it.

2. Install Libraries
Install the necessary Python libraries using pip:

sudo pip3 install Adafruit_DHT adafruit-circuitpython-ssd1306 Pillow
sudo pip3 install adafruit-blinka # Required for CircuitPython compatibility

3. Clone the Repository
Clone this project to your Raspberry Pi:

git clone <your-repository-url>
cd <your-repository-name>

(Replace <your-repository-url> and <your-repository-name> with your actual repository details.)

Wiring
Connect the components as follows:

DHT11 Sensor
DHT11 VCC: To Raspberry Pi 3.3V (Pin 1)

DHT11 GND: To Raspberry Pi GND (Pin 6 or any GND pin)

DHT11 Data: To Raspberry Pi GPIO4 (Pin 7)

SSD1306 OLED Display
OLED VCC: To Raspberry Pi 3.3V (Pin 1)

OLED GND: To Raspberry Pi GND (Pin 9 or any GND pin)

OLED SCL: To Raspberry Pi SCL (Pin 5)

OLED SDA: To Raspberry Pi SDA (Pin 3)

Usage
To run the script, navigate to the project directory and execute the Python script:

python3 main.py

(Assuming your main script is named main.py)

The OLED display should start showing the temperature readings. If the sensor cannot be read, it will display "Sensor Error".
