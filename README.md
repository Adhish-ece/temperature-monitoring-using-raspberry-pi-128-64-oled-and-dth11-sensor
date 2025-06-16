```
# DHT11 Temperature Display on OLED using Raspberry Pi

This project reads temperature data from a **DHT11** sensor and displays it on a **128x64 OLED** screen using a **Raspberry Pi**. The data is updated every 5 seconds.

## 📷 Project Overview

- Reads temperature from a DHT11 sensor connected to GPIO4.
- Displays the temperature on an SSD1306 OLED via I2C.
- Uses the Raspberry Pi's I2C and GPIO capabilities.
- Displays "Sensor Error" if the DHT11 fails to respond.

## 🛠️ Hardware Requirements

- Raspberry Pi (any model with GPIO support)
- DHT11 Temperature and Humidity Sensor
- SSD1306 128x64 OLED Display (I2C)
- Jumper Wires

## 💻 Software Requirements

Install the following Python libraries before running the code:

```
pip install Adafruit_DHT
pip install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil
```

Additionally, make sure I2C is enabled on your Raspberry Pi:

```
sudo raspi-config
# Navigate to: Interface Options > I2C > Enable
```

## 🧾 How to Run

1. Connect the DHT11 sensor to GPIO4.
2. Connect the OLED screen to the I2C pins (SCL to GPIO3, SDA to GPIO2).
3. Save the script as `temperature_display.py`.
4. Run the script:

```
python3 temperature_display.py
```

## 🖼️ Output Example

- OLED will display: `24.0°C` (example temperature).
- Console will log the same value or print `Sensor Error` if the sensor fails.

## 📁 File Structure

```
├── temperature_display.py
└── README.md
```

## 📌 Notes

- The font used is `DejaVuSans-Bold.ttf` located at `/usr/share/fonts/truetype/dejavu/`.
- You can adjust the font size or text position as needed based on your OLED resolution.

## 📃 License

This project is open-source and available under the MIT License.
```
