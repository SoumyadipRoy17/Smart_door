// #include <Servo.h>

// Servo myservo;
// int pos = 0; 

// void setup() {
//     Serial.begin(9600);  // Baud rate for serial communication
//     myservo.attach(9);
//     myservo.write(pos);  // Initialize servo position
//     Serial.println("Servo initialized at 0°");
// }

// void loop() {
//     if (Serial.available() > 0) {
//         String char_data = Serial.readString();
//         char_data.trim();  // Remove extra whitespace and newline characters

//         Serial.print("Received command: ");
//         Serial.println(char_data);

//         if (char_data == "ON") {
//             for (int angle = 10; angle <= 180; angle++) { 
//                 myservo.write(angle);
//                 delay(15);
//             }
//         } 
//         else if (char_data == "OFF") {  // Reset to 0° if needed
//             for (int angle = 180; angle >= 0; angle--) { 
//                 myservo.write(angle);
//                 delay(15);
//             }
//         }
//     }
// }

// #include <Servo.h>

// Servo myservo;
// int pos = 0;  
// const int ldrPin = A0;  // LDR sensor connected to A0
// const int ledPin = 7;   // LED connected to D7
// int lightThreshold = 300;  // Adjust based on room lighting

// void setup() {
//    Serial.begin(9600);  
//     myservo.attach(9);
//     myservo.write(pos);  // Initialize servo position
//     pinMode(ledPin, OUTPUT);  // Set LED pin as output
//     Serial.println("System Initialized");
// }

// void loop() {
//     // Read LDR value
//     int ldrValue = analogRead(ldrPin);
//     // Serial.print("LDR Value: ");
//     // Serial.println(ldrValue);
//       if (ldrValue < lightThreshold) {
//             digitalWrite(ledPin, HIGH);
//             delay(1000);
//         }
//         else
//         {
//            digitalWrite(ledPin, LOW);
//             delay(1000);

//         }
   

//     // Servo control through Serial commands
//     if (Serial.available() > 0) {
//         String char_data = Serial.readString();
//         Serial.flush();
//         char_data.trim();  // Remove extra whitespace and newline characters

//         Serial.print("Received command: ");
//         Serial.println(char_data);

//         if (char_data == "ON") {
//             for (int angle = 10; angle <= 180; angle++) { 
//                 myservo.write(angle);
//                 delay(15);
//             }

//              // // Turn LED ON if it's dark
       
//         } 
//         else if (char_data == "OFF") {  
//             for (int angle = 180; angle >= 0; angle--) { 
//                 myservo.write(angle);
//                 delay(15);
//             }

//             // digitalWrite(ledPin,LOW);
//             // delay(5000);
//         }
//     }
// }


#include <Servo.h>

Servo myservo;
int pos = 0;  
const int ldrPin = A0;  // LDR sensor connected to A0
const int ledPin = 7;   // LED connected to D7
int lightThreshold = 300;  // Adjust based on room lighting
bool ldrActive = false;  // Flag to enable/disable LDR functionality

void setup() {
    Serial.begin(9600);  
    myservo.attach(9);
    myservo.write(pos);  // Initialize servo position
    pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
    // Control LDR only if activated by "ON" command
    if (ldrActive) {
        int ldrValue = analogRead(ldrPin);
        if (ldrValue < lightThreshold) {
            digitalWrite(ledPin, HIGH);
        } else {
            digitalWrite(ledPin, LOW);
        }
    } else {
        digitalWrite(ledPin, LOW);  // Ensure LED remains off when LDR is disabled
    }

    // Servo control through Serial commands
    if (Serial.available() > 0) {
        String char_data = Serial.readString();
        Serial.flush();
        char_data.trim();  // Remove extra whitespace and newline characters

        if (char_data == "ON") {
            ldrActive = true;  // Enable LDR functionality
            for (int angle = 10; angle <= 180; angle++) { 
                myservo.write(angle);
                delay(15);
            }
        } 
        else if (char_data == "OFF") {  
            ldrActive = false;  // Disable LDR functionality
            for (int angle = 180; angle >= 0; angle--) { 
                myservo.write(angle);
                delay(15);
            }
        }
    }
}
