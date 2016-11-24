#include "Arduino.h"
#include "EEPROM.h"

byte incoming;

const char buzzer=9;
const char button=12;
const char leftM_In1=2;
const char leftM_In2=4;
const char leftM_PWM=5;
const char rightM_In1=7;
const char rightM_In2=8;
const char rightM_PWM=6;
const char rightW=A5;
const char leftW=A4;
const char encodeR=10;
const char encodeL=A2;
const char servo=A1;

void setup() {
  Serial.begin(9600);

  pinMode(button,INPUT_PULLUP);
  pinMode(buzzer,OUTPUT);

  //initU();

  pinMode(leftM_In1,OUTPUT);
  pinMode(leftM_In2,OUTPUT);
  pinMode(leftM_PWM,OUTPUT);
  pinMode(rightM_In1,OUTPUT);
  pinMode(rightM_In2,OUTPUT);
  pinMode(rightM_PWM,OUTPUT);

  pinMode(rightW,INPUT);
  pinMode(leftW,INPUT);
  pinMode(encodeR,INPUT_PULLUP);
  pinMode(encodeL,INPUT_PULLUP);

  pinMode(servo,OUTPUT);
}

void loop() {
  while (Serial.available()>0) {
    incoming=Serial.read();
    Serial.write(incoming);
  }
}
