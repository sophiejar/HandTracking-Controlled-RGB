#define PIN_R 9
#define PIN_G 10
#define PIN_B 11

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  
  pinMode(PIN_R, OUTPUT);
  pinMode(PIN_G, OUTPUT);
  pinMode(PIN_B, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    
    int rVal = Serial.parseInt();
    int gVal = Serial.parseInt();
    int bVal = Serial.parseInt();

    if (Serial.read() == '\n') {
      // Optional: Logic can go here if needed
    }

    updateLedColor(rVal, gVal, bVal);
  }
}


void updateLedColor(int r, int g, int b) {
  analogWrite(PIN_R, r);
  analogWrite(PIN_G, g);
  analogWrite(PIN_B, b);
}
