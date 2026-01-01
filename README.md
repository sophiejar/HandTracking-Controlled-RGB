# 🖐️ Hand-Link: AI Gesture-Controlled RGB Lighting

**Hand-Link** is a computer vision project that uses **MediaPipe** and **OpenCV** to track your hand gestures to control a physical RGB LED. Change colors, adjust brightness, and toggle effects in real-time.

---

## 🛠️ Hardware & Wiring
Connect your Common Cathode RGB LED to your Arduino as follows:
* **Red Pin:** Arduino Pin 9 (with 220Ω resistor)
* **Green Pin:** Arduino Pin 10 (with 220Ω resistor)
* **Blue Pin:** Arduino Pin 11 (with 220Ω resistor)
* **Cathode (Long Leg):** Ground (GND)

---

## 🚀 Setup & Usage (Step-by-Step)

### 1. Prepare the Hardware
Upload the `.ino` code in the `HandtrackingRGBControl` folder to your Arduino board. **Important:** Make sure the Serial Monitor in the Arduino IDE is closed before moving to the next step.

### 2. Install Dependencies
Run this command in your terminal/command prompt to install the required Python libraries:
pip install opencv-python mediapipe pyserial numpy

### 3. **Run the System**
Open the main.py file and verify that the SERIAL_PORT matches your Arduino (e.g., 'COM3'). Then, run:
python handcolor.py
- - - - - - - - - - - - - - - - - - - - - - - - 
### 🎮 **Controls**
Once the camera window opens, use these gestures:

**Change Color**: Move your index finger across the gradient bar at the top.

**Brightness**: Slide your finger up and down on the left side of the screen.

**Strobe/Off**: Make a fist to toggle the light state.

**Exit**: Press the 'X' key on your keyboard to close everything.

### 📂 **Project Structure**
HandtrackingRGBControl/ — Contains the Arduino code.

handcolor.py — The core Python vision and serial engine.

requirements.txt — List of dependencies.

README.md — This documentation.

### ⚠️ **Troubleshooting**
**Serial Error**: Ensure no other program (like Arduino IDE) is using the COM port.

**Flickering**: Ensure you are in a well-lit room for accurate finger tracking.

**Wrong Colors**: Swap the pin numbers in the Arduino code if Red/Green/Blue are mixed up.

### 📜 **License**

This project is licensed under the MIT License.
