```
# DHT11 Temperature Display on OLED using Raspberry Pi

This project reads temperature data from a **DHT11** sensor and displays it on a 128x64 OLED screen using a Raspberry Pi. The data is updated every 5 seconds.

## 📥 Clone the Repository

First, clone this repository:

```
git clone https://github.com/Adhish-ece/temperature-monitoring-using-raspberry-pi-128-64-oled-and-dth11-sensor.git

```
cd temperature-monitoring-using-raspberry-pi-128-64-oled-and-dth11-sensor

## 🛠️ Hardware Requirements

- Raspberry Pi (any model with GPIO support)
- DHT11 Temperature and Humidity Sensor
- SSD1306 128x64 OLED Display (I2C)
- Jumper Wires

## 💻 Software Installation

Install all dependencies from the `requirements.txt` file:

```
pip install -r requirements.txt
```

Make sure I2C is enabled on your Raspberry Pi:

```
sudo raspi-config
# Navigate to: Interface Options > I2C > Enable
```

## ▶️ How to Run

Execute the script:

```
python3 display.py
```

## 🖼️ Output Example

- OLED will display: `24.0°C` (example temperature).
- Console will log the same value or print `Sensor Error` if the sensor fails.

## 📁 File Structure

```
├── display.py
├── requirements.txt
└── README.md
```

## 📌 Notes

- The font used is `DejaVuSans-Bold.ttf` located at `/usr/share/fonts/truetype/dejavu/`.
- You can adjust the font size or text position as needed based on your OLED resolution.
```
