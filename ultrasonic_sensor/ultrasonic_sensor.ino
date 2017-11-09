// Turns on LED in ultrasonic sensor senses anything within 50cm
// Button displays text when pressed

#include "SR04.h"
#define TRIG_PIN 5 
#define ECHO_PIN 3 

// Define RGB LED Pins
#define RED 9
#define GREEN 10
#define BLUE 11

SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
long a;

int distanceLED = 8; // red LED
bool pauseDistanceLED = false;
int button = 2;
char userInput;
bool faceDetected = false;
bool indicateNoFaceDetection = false;

void setup() {
  Serial.begin(9600);
  delay(1000);

  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  
  pinMode(distanceLED, OUTPUT);
  digitalWrite(distanceLED, LOW);

  pinMode(button, INPUT_PULLUP);
}

void loop() {
  
  checkSerial();
  
  if(faceDetected){
    copLED();
  }
  if(indicateNoFaceDetection){
    flashGreen();
    RGBoff();
    indicateNoFaceDetection = false;
  }

  // if button is pressed, start detecting objects again
  if(digitalRead(button) == LOW) {
    RGBoff();
    pauseDistanceLED = false;
    faceDetected = false;
    Serial.println("PROGRAM RESET");
    delay(500);
  }
  
  a=sr04.Distance();

  // if object was not recently detected, keep checking distance
  if(!pauseDistanceLED){
    checkDistance(a);
    Serial.print(a);
    Serial.println("cm");
    delay(500);
  }
  
  //setRandomRGBcolor();
}

void checkDistance(int distance) {
  if(distance <= 50) {
    digitalWrite(distanceLED, HIGH);  
  }
  else if(distance > 50) {
    digitalWrite(distanceLED, LOW);
  }
}

// used to halt red LED and indicate image is being processed when object is <= 50cm from sensor
void checkSerial() {
  if(Serial.available() > 0){
    userInput = Serial.read();
    if(userInput == 'd'){   // object is detected
      digitalWrite(distanceLED, LOW);
      pauseDistanceLED = true;          // stop checking distance
      delay(1000);
      Serial.println("Image is being taken and processed...");
      RGByellow();
    }
    else if(userInput == 'y'){    // face is dectected
      faceDetected = true; 
    }
    else if(userInput == 'n'){    // face is not dectected
      faceDetected = false; 
      indicateNoFaceDetection = true;
    }
    /*
    else if(userInput == 'r'){    // face is not dectected
      faceDetected = false; 
      pauseDistanceLED = false;
      //Serial.println("RESTARTED PROGRAM!");
    }
    */
  }
}

void copLED(){    // sets red and blue leds flashing
  RGBoff();
  analogWrite(BLUE, 5);
  delay(500);
  RGBoff(); 
  digitalWrite(distanceLED, HIGH);
  delay(500);
  digitalWrite(distanceLED, LOW);
}

// ---------------- Functions for RGB LED ----------------

void RGByellow(){
  analogWrite(RED, 5);
  analogWrite(GREEN, 5);
  analogWrite(BLUE, 0);
}
void RGBoff(){  // turns off RGB LED
  analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 0);
}
void flashGreen(){
  RGBoff();
  analogWrite(GREEN, 5);
  delay(500);
  analogWrite(GREEN, 0);
  delay(500);
  analogWrite(GREEN, 5);
  delay(500);
  analogWrite(GREEN, 0);
  delay(500);
}
void setRandomRGBcolor() {
  int redValue = random(255);  // need 3 random number between 1 and 255
  int greenValue = random(255);
  int blueValue = random(255);

  // simply outputs a random color
  analogWrite(RED, redValue);
  analogWrite(GREEN, blueValue);
  analogWrite(BLUE, greenValue);
  delay(1000);
}

