# ESP8266 Hydroponics Monitoring System

This project is an IoT-based hydroponics monitoring system using an ESP8266 microcontroller. The ESP8266 hosts a web server that provides real-time sensor data for monitoring parameters like TDS, pH, humidity, water temperature, and air temperature.

## Features
- Real-time monitoring of hydroponics system parameters
- Web interface to fetch and display sensor data
- API endpoints to retrieve sensor data
- ESP8266 WiFi connection for remote access

## Hardware Requirements
- ESP8266 (e.g., NodeMCU)
- TDS Sensor
- pH Sensor
- DHT11/DHT22 (for humidity and temperature)
- Power supply (e.g., 5V USB adapter)
- Jumper wires
- Breadboard (optional)

## Software Requirements
- Arduino IDE
- ESP8266 board library installed in Arduino IDE
- Required dependencies:
  - ESP8266WiFi
  - ESP8266WebServer

## Installation Guide
### 1. Setting Up the ESP8266
1. Install [Arduino IDE](https://www.arduino.cc/en/software).
2. Open Arduino IDE and go to **File > Preferences**.
3. In the "Additional Board Manager URLs" field, add:
   ```
   http://arduino.esp8266.com/stable/package_esp8266com_index.json
   ```
4. Go to **Tools > Board > Boards Manager**, search for **ESP8266**, and install it.
5. Connect the ESP8266 to your computer via USB.
6. Select the correct board (**NodeMCU 1.0** or your specific ESP8266 model) and COM port.
7. Install required libraries in Arduino IDE via **Sketch > Include Library > Manage Libraries**:
   - Search for **ESP8266WiFi** and install it.
   - Search for **ESP8266WebServer** and install it.
8. Upload the provided ESP8266 code to the board.

### 2. Setting Up the Web Application
1. Install Python and Django (if not already installed):
   ```sh
   pip install django
   ```
2. Clone the project repository:
   ```sh
   git clone https://github.com/your-repository/esp8266-hydroponics.git
   cd esp8266-hydroponics
   ```
3. Start the Django server:
   ```sh
   python manage.py runserver
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```
5. Enter the ESP8266 IP address in the input field and fetch the sensor data.

## API Endpoints
### 1. Fetch Sensor Data
- **URL:** `http://ESP_IP/sensor-data`
- **Method:** `GET`
- **Response:** JSON with sensor values
  ```json
  {
    "TDS": 800.5,
    "pH": 6.5,
    "Humidity": 75.2,
    "WaterTemp": 22.3,
    "AirTemp": 30.1
  }
  ```

## Troubleshooting
- **ESP8266 not connecting to WiFi?**
  - Check SSID and password in the code.
  - Ensure your router is in 2.4GHz mode (ESP8266 does not support 5GHz).
- **CORS policy error when fetching data?**
  - Ensure the ESP8266 server sends proper CORS headers.
- **ESP8266 not responding to requests?**
  - Verify the ESP8266 IP address and ensure it is in the same network as your system.

## License
This project is open-source and available under the MIT License.
