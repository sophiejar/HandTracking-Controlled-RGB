import cv2
import mediapipe as mp
import serial
import time
import numpy as np
from collections import deque

# --- Configuration & Hardware ---
SERIAL_PORT = 'COM3'
BAUD_RATE   = 9600
FRAME_W     = 1280
FRAME_H     = 720

class GestureInterface:
    def __init__(self):
        # Initialize Serial Link
        try:
            self.device = serial.Serial(SERIAL_PORT, BAUD_RATE)
            time.sleep(2)
        except:
            self.device = None
            print("Running in simulation mode (No Arduino)")

        # MediaPipe Setup
        self.mp_hands = mp.solutions.hands
        self.hand_engine = self.mp_hands.Hands(
            max_num_hands=1, 
            min_detection_confidence=0.7, 
            min_tracking_confidence=0.7
        )

        # State Variables
        self.rgb_current = [0, 255, 255]
        self.lumen_level = 1.0
        self.coord_history = deque(maxlen=8)
        self.is_strobe = False
        self.timer_mark = 0

        # UI Element Generation
        self.grad_w, self.grad_h = 800, 25
        self.grad_x = (FRAME_W - self.grad_w) // 2
        self.grad_y = 50
        self.color_map = self._generate_ui_gradient()

    def _generate_ui_gradient(self):
        """Creates the BGR color strip for the UI"""
        strip = np.zeros((self.grad_h, self.grad_w, 3), dtype=np.uint8)
        for i in range(self.grad_w):
            hue = int(i / self.grad_w * 180)
            strip[:, i] = cv2.cvtColor(np.uint8([[[hue, 255, 255]]]), cv2.COLOR_HSV2BGR)[0][0]
        return strip

    def update_logic(self, frame):
        """Main processing logic for gesture detection and serial output"""
        frame = cv2.flip(frame, 1)
        ui_layer = np.zeros_like(frame)
        
        # Hand Tracking
        results = self.hand_engine.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        fist_active = False

        if results.multi_hand_landmarks:
            marks = results.multi_hand_landmarks[0].landmark
            
            # Map Landmark Points
            root = np.array([marks[0].x * FRAME_W, marks[0].y * FRAME_H])
            tip1 = np.array([marks[8].x * FRAME_W, marks[8].y * FRAME_H])
            tip2 = np.array([marks[12].x * FRAME_W, marks[12].y * FRAME_H])
            tip3 = np.array([marks[16].x * FRAME_W, marks[16].y * FRAME_H])

            # Fist Recognition
            avg_span = sum([np.linalg.norm(root - p) for p in [tip1, tip2, tip3]]) / 3
            if avg_span < 130:
                fist_active = True
                if (time.time() - self.timer_mark) > 0.08:
                    self.is_strobe = not self.is_strobe
                    self.timer_mark = time.time()
            else:
                self.is_strobe = False

            # Screen Interaction
            self.coord_history.append(tip1)
            px = int(np.mean([p[0] for p in self.coord_history]))
            py = int(np.mean([p[1] for p in self.coord_history]))

            # UI Collision Detection
            if self.grad_y - 30 < py < self.grad_y + self.grad_h + 30 and \
               self.grad_x < px < self.grad_x + self.grad_w:
                self.rgb_current = [int(c) for c in self.color_map[0, np.clip(px - self.grad_x, 0, self.grad_w - 1)]]

            if 10 < px < 110 and 200 < py < 550:
                self.lumen_level = np.clip(1.0 - (py - 200) / 350, 0.05, 1.0)

            # Draw Hand Connections
            for link in self.mp_hands.HAND_CONNECTIONS:
                p1 = (int(marks[link[0]].x * FRAME_W), int(marks[link[0]].y * FRAME_H))
                p2 = (int(marks[link[1]].x * FRAME_W), int(marks[link[1]].y * FRAME_H))
                cv2.line(ui_layer, p1, p2, (0, 255, 0) if fist_active else (200, 200, 200), 1)

        # Final Color Processing
        b_in, g_in, r_in = self.rgb_current
        r_out, g_out, b_out = (0, 0, 0) if self.is_strobe else \
                              (int(r_in * self.lumen_level), 
                               int(g_in * self.lumen_level), 
                               int(b_in * self.lumen_level))

        # Send to Arduino
        if self.device:
            self.device.write(f"{r_out},{g_out},{b_out}\n".encode())

        # HUD Rendering
        ui_layer[self.grad_y:self.grad_y+self.grad_h, self.grad_x:self.grad_x+self.grad_w] = self.color_map
        cv2.rectangle(ui_layer, (60, 200), (80, 550), (30, 30, 30), -1)
        
        fill_y = int(550 - (self.lumen_level * 350))
        bar_col = (b_in, g_in, r_in) if not self.is_strobe else (0,0,0)
        cv2.rectangle(ui_layer, (60, fill_y), (80, 550), bar_col, -1)
        
        cv2.putText(ui_layer, f"POWER: {int(self.lumen_level*100)}%", (45, 180), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return cv2.addWeighted(frame, 0.6, ui_layer, 1.0, 0)

# --- Runtime Execution ---
if __name__ == "__main__":
    controller = GestureInterface()
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)

    while True:
        status, raw_frame = capture.read()
        if not status: break
        
        display_img = controller.update_logic(raw_frame)
        cv2.imshow("System Control", display_img)
        
        # Press 'x' to shut down
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    capture.release()
    cv2.destroyAllWindows()
