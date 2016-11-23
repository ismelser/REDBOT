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

int pos = 90; //EEPROM.read(0);
int hold=0;
int uTime=0;

void initU() {
  tone(buzzer, 440);
  delay(30);
  tone(buzzer, 880);
  delay(100);
  noTone(buzzer);
}


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

  initU();
}
void loop() {
  while (Serial.available()>0){
    incoming=Serial.read();
    initU();
    pos=incoming;
  }
  if (pos<0) {
    pos=10;
  }
  if (pos>180) {
    pos=170;
  }
  //EEPROM.write(0, pos);
  //if (micros()-uTime<6000000) {
    digitalWrite(servo,HIGH);
    delayMicroseconds(((pos*(1.5/180.0))+0.75)*1000);
    digitalWrite(servo,LOW);
    delayMicroseconds(20000-(((pos*(1.5/180.0))+0.75)*1000));
  //}
}

