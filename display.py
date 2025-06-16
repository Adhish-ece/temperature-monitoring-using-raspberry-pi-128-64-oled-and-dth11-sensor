import time
import Adafruit_DHT
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# DHT11 configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO4

# I2C OLED config
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear screen
oled.fill(0)
oled.show()

# Image for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)  # Clear screen

    if temperature is not None:
        # Show actual decimal value from sensor
        temp_text = "{:.1f}°C".format(temperature)
        print(f"Temperature: {temp_text}")
        draw.text((20, 20), temp_text, font=font, fill=255)
    else:
        draw.text((10, 20), "Sensor Error", font=font, fill=255)
        print("Sensor Error")

    oled.image(image)
    oled.show()

    time.sleep(5)

