// //LDR gives out analog voltage when connected to 5v(VCC)

// //servo motor 
// #include <Servo.h> 
// Servo myservo;  // create servo object to control a servo
// int pos = 0;

// //ldr and bulb control pins
// const int ledPin=2;
// const int ldrPin=A0; //analog input

// void setup()
// {
//   Serial.begin(9600);
  
// //  pinMode(ledPin,OUTPUT);
// //  pinMode(ldrPin,INPUT);
  
//   myservo.attach(9);
//   myservo.write(pos);
// }
// void loop()
// {
//     //Control Bulb based on LDR
// //  int ldrStatus=analogRead(ldrPin);
// //  Serial.println(ldrStatus);
// //  if(ldrStatus<=550)   //when it's dark less conductivity(low voltage)
// //  {
// //    digitalWrite(ledPin,1);
// //    Serial.println("Dark outside, Bulb is ON");
// //  }
// //  else
// //  {
// //    digitalWrite(ledPin,0);
// //    Serial.println("Bright outside");
// //  }
  
  
//     //Unlock and lock door(servo motor mechanism) based on Face Recognition
//   if(Serial.available())
//   {
//     char char_data=Serial.read(); //read one byte from serial buffer and save it to the variable
//     if(char_data=='o')
//     {
//       openlock();
//     }
//     else if(char_data=='c')
//     {
//       closelock();
//     }
//     delay(500);
//   }  
// }

// void openlock()
// {
//   if(pos==0)
//   {
//     pos=90;
//     myservo.write(pos);
//     Serial.println("DOOR OPEN");
//   }
//   else
//   {
//     Serial.println("DOOR ALREADY OPEN");
//   }
// }

// void closelock()
// {
//   if(pos==90)
//   {
//     pos=0;
//     myservo.write(pos);
//     Serial.println("Door CLOSED");
//   }
//   else
//   {
//     Serial.println("DOOR ALREADY CLOSED");
//   }
// }
//LDR gives out analog voltage when connected to 5v(VCC)

// //servo motor 
// #include <Servo.h> 
// Servo myservo;  // create servo object to control a servo
// int pos = 0;

// //ldr and bulb control pins
// const int ledPin=13;
// const int ldrPin=A5; //analog input

// void setup()
// {
//   Serial.begin(9600);
  
//   pinMode(ledPin,OUTPUT);
//   pinMode(ldrPin,INPUT);
  
//   myservo.attach(9);
//   myservo.write(pos);
// }
// void loop()
// {
//     //Control Bulb based on LDR
//   int ldrStatus=analogRead(ldrPin);
//   Serial.println(ldrStatus);
//   if(ldrStatus<=550)   //when it's dark less conductivity(low voltage)
//   {
//     digitalWrite(ledPin,1);
//     Serial.println("Dark outside, Bulb is ON");
//   }
//   else
//   {
//     digitalWrite(ledPin,0);
//     Serial.println("Bright outside");
//   }
  
  
//     //Unlock and lock door(servo motor mechanism) based on Face Recognition
//   if(Serial.available())
//   {
//     char char_data=Serial.read(); //read one byte from serial buffer and save it to the variable
//     while (Serial.available()) Serial.read();
//     if(char_data=='o')
//     {
//       openlock();
//     }
//     else if(char_data=='c')
//     {
//       closelock();
//     }
//     delay(500);
//   }  
// }

// void openlock()
// {
  
//     pos=180;
//     myservo.write(pos);
//     Serial.println("DOOR OPEN");
  

//     Serial.println("DOOR ALREADY OPEN");
  
// }

// void closelock()
// {
//   if(pos==90)
//   {
//     pos=0;
//     myservo.write(pos);
//     Serial.println("Door CLOSED");
//   }
//   else
//   {
//     Serial.println("DOOR ALREADY CLOSED");
//   }
// }

// #include <Servo.h> 

// Servo myservo;  // create servo object to control a servo
// int pos = 0;

// void setup() {
//   Serial.begin(9600);
//   myservo.attach(9);
//   myservo.write(pos); // Initialize servo position
//   Serial.println("Servo initialized");
// }

// void loop() {
//     // Check for serial input
//     if (Serial.available()) {
//         char char_data = Serial.read(); // Read one byte from serial buffer
//         while (Serial.available()) Serial.read(); // Clear any extra bytes in buffer

//         Serial.print("Received command: ");
//         Serial.println(char_data);

//         if (char_data == 'o') {
//             openlock();
//         } 
//         else if (char_data == 'c') {
//             closelock();
//         }
//     }
// }

// void openlock() {
//     if (pos != 180) {  // Only move if not already open
//         pos = 180;
//         myservo.write(pos);
//         Serial.println("DOOR OPEN");
//         delay(2000);  // Allow servo to move
//     } else {
//         Serial.println("DOOR ALREADY OPEN");
//     }
// }

// void closelock() {
//     if (pos != 0) {  // Only move if not already closed
//         pos = 0;
//         myservo.write(pos);
//         Serial.println("Door CLOSED");
//         delay(1000);  // Allow servo to move
//     } else {
//         Serial.println("DOOR ALREADY CLOSED");
//     }
// }

// #include <Servo.h>

// Servo servo;
// int angle = 10;

// void setup() {
//   servo.attach(8);
//   servo.write(angle);
// }


// void loop() 
// { 
//  // scan from 0 to 180 degrees
//   for(angle = 10; angle < 180; angle++)  
//   {                                  
//     servo.write(angle);               
//     delay(15);                   
//   } 
//   // now scan back from 180 to 0 degrees
//   for(angle = 180; angle > 10; angle--)    
//   {                                
//     servo.write(angle);           
//     delay(15);       
//   } 
// }
#include <Servo.h> 

Servo myservo;  
int pos = 0;
int angle = 10;

void setup() {
    Serial.begin(115200); // Increased baud rate for reliability
    myservo.attach(9);
    myservo.write(pos);
    Serial.println("Servo initialized at 0°");
}

void loop() {
    if (Serial.available() > 0) {
        char char_data = Serial.read();
        Serial.print("Received command: ");
        Serial.println(char_data);

        if (char_data == 'o') {

            openlock();
        } 
        else if (char_data == 'c') {
            closelock();
        }
    }
}

void openlock() {
    Serial.println("Opening Door...");
   //now scan back from 180 to 0 degrees
  for(angle = 180; angle > 10; angle--)    
  {                                
    myservo.write(angle);           
    delay(15);       
  } 
    delay(1000);  // Allow servo time to move
    Serial.println("Door is OPEN");
}

void closelock() {
    Serial.println("Closing Door...");
 for(angle = 0; angle <= 180; angle++)    
  {                                
    myservo.write(angle);           
    delay(15);       
  } 
    myservo.write(0);
    delay(1000);
    Serial.println("Door is CLOSED");
}
