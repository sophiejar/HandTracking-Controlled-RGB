 🖐️ Hand-Link: AI Gesture-Controlled RGB Lighting

An interactive computer vision project that bridges the gap between digital gestures and physical hardware. Control your room's ambiance using nothing but your hands.

---

## ✨ Features
- **Real-time Tracking:** Powered by **MediaPipe** for high-accuracy hand landmark detection.
- **Interactive HUD:** On-screen color picker and vertical brightness slider.
- **Gesture Shortcuts:** Toggle "Strobe Mode" (Blackout) by simply making a fist.
- **Low Latency:** Optimized Serial communication (9600 Baud) for instant LED response.

---

## 🛠️ Hardware Requirements
- **Arduino** (Uno, Nano, or Mega)
- **Common Cathode RGB LED**
- **3x 220Ω Resistors**
- **Breadboard & Jumper Wires**

### 🔌 Wiring Guide
Connect your LED to the following Arduino Pins:
* **Red Pin:** Pin 9 (via 220Ω resistor)
* **Green Pin:** Pin 10 (via 220Ω resistor)
* **Blue Pin:** Pin 11 (via 220Ω resistor)
* **Longest Pin (Cathode):** Connect to **GND**

---

## 💻 Software Setup

### 1. Arduino Installation
1. Open the `.ino` file located in the project folder using the Arduino IDE.
2. Ensure your board is connected and select the correct **COM Port**.
3. Click **Upload**.

### 2. Python Installation
1. Ensure you have Python 3.8+ installed.
2. Install the necessary libraries:
   ```bash
   pip install opencv-python mediapipe pyserial numpy
Open the Python script and verify the SERIAL_PORT variable (e.g., 'COM3') matches your Arduino.Run the application:Bashpython main.py
🎮 How to ControlActionGestureChange ColorMove your index finger across the top color barAdjust BrightnessSlide your hand up/down on the left side of the screenToggle StrobeMake a fist with your handExit AppPress the 'X' key on your keyboard📂 Project StructureHandtrackingRGBControl/ — Contains the Arduino firmware and Python logic.README.md — Project documentation.📜 LicenseThis project is open-source and available under the MIT License.
