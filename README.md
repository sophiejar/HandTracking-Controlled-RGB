# 🖐️ HandControlled: AI-Powered RGB Interface

**Gesture-Link** is an AI project that tracks your hand landmarks to control an RGB LED. Use on-screen sliders for color/brightness and gestures for special effects.

## 🛠️ Hardware Setup

* **Red Pin:** Pin 9 (with 220Ω resistor)
* **Green Pin:** Pin 10 (with 220Ω resistor)
* **Blue Pin:** Pin 11 (with 220Ω resistor)
* **Cathode:** GND

## 🚀 Quick Start
1. **Upload Firmware:** Flash the Arduino code to your board.
2. **Install Python Libs:** `pip install opencv-python mediapipe pyserial numpy`
3. **Run App:** Execute `python main.py`

## 🎮 Controls
* **Index Finger:** Move across top bar to change color.
* **Vertical Move:** Slide on the left side to change brightness.
* **Fist:** Toggle Strobe/Blackout mode.
* **'X' Key:** Exit the program.
