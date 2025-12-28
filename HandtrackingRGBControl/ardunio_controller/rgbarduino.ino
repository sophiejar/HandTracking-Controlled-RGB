// Define PWM pins for the LED channels
#define PIN_R 9
#define PIN_G 10
#define PIN_B 11

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  
  // Set all LED pins as outputs
  pinMode(PIN_R, OUTPUT);
  pinMode(PIN_G, OUTPUT);
  pinMode(PIN_B, OUTPUT);
}

void loop() {
  // Check if data is waiting in the serial buffer
  if (Serial.available() > 0) {
    
    // Use parseInt to directly extract integers separated by commas
    int rVal = Serial.parseInt();
    int gVal = Serial.parseInt();
    int bVal = Serial.parseInt();

    // After reading values, clear the rest of the buffer (newline character)
    if (Serial.read() == '\n') {
      // Optional: Logic can go here if needed
    }

    // Apply the intensities to the RGB LED using PWM
    updateLedColor(rVal, gVal, bVal);
  }
}

/**
 * Helper function to apply colors to the pins
 */
void updateLedColor(int r, int g, int b) {
  analogWrite(PIN_R, r);
  analogWrite(PIN_G, g);
  analogWrite(PIN_B, b);
}