
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
//////////////////////////////////////////
void setup() {
  Serial.begin(9600);
  interrupts();

  
  pinMode(button,INPUT_PULLUP);
  pinMode(buzzer,OUTPUT);

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
//////////////////////////////////////////
int turn=270;
void loop() {
  while (digitalRead(button)==HIGH) {}
  delay(500);
  forward(1000,255);
  mStop();
  turnRight(turn,255);
  //delay(420); table top
  mStop();
  forward(1000,255);
  mStop();
  turnRight(turn,255);
  mStop();
  forward(1000,255);
  mStop();
  turnRight(turn,255);
  mStop();
  forward(1000,255);
  mStop();
  turnRight(turn,255);
  mStop();
  initU();
  //delay(410); table top
}

void alt() {
  while (digitalRead(button)==HIGH) {}
  for (int i; i<100; i++) {
    int right=sin(i/3.14)*100+150;
    int left=cos(i/5)*100+150;
    motorControl(right,left,100);
  }
  mStop();
}
//////////////////////////////////////////
void initU() {
  tone(buzzer,440);
  delay(50);
  tone(buzzer,880);
  delay(100);
  noTone(buzzer);
  delay(1000);
}
//////////////////////////////////////////
void forward(int udelay,int value) {
  digitalWrite(rightM_In1,LOW);
  digitalWrite(rightM_In2,HIGH);
  digitalWrite(leftM_In1,HIGH);
  digitalWrite(leftM_In2,LOW);
  digitalWrite(leftM_PWM,abs(value));
  digitalWrite(rightM_PWM,abs(value));
  delay(udelay);
}
void backwards(int udelay,int value) {
  digitalWrite(rightM_In1,HIGH);
  digitalWrite(rightM_In2,LOW);
  digitalWrite(leftM_In1,LOW);
  digitalWrite(leftM_In2,HIGH);
  digitalWrite(leftM_PWM,abs(value));
  digitalWrite(rightM_PWM,abs(value));
  delay(udelay);
}
void turnRight(int udelay,int value) {
  digitalWrite(leftM_In1,HIGH);
  digitalWrite(leftM_In2,LOW);
  digitalWrite(rightM_In1,HIGH);
  digitalWrite(rightM_In2,LOW);
  digitalWrite(leftM_PWM,abs(value));
  digitalWrite(rightM_PWM,abs(value));
  delay(udelay);
}
void turnLeft(int udelay,int value) {
  digitalWrite(leftM_In1,LOW);
  digitalWrite(leftM_In2,HIGH);
  digitalWrite(rightM_In1,LOW);
  digitalWrite(rightM_In2,HIGH);
  digitalWrite(leftM_PWM,abs(value));
  digitalWrite(rightM_PWM,abs(value));
  delay(udelay);
}
void motorControl(int right, int left, int udelay) {
  if (right>0) {
    digitalWrite(rightM_In1,LOW);
    digitalWrite(rightM_In2,HIGH);
  }
  else {
    digitalWrite(rightM_In1,HIGH);
    digitalWrite(rightM_In2,LOW);
  }
  if (left>0) {
    digitalWrite(leftM_In1,HIGH);
    digitalWrite(leftM_In2,LOW);
  }
  else {
    digitalWrite(leftM_In1,LOW);
    digitalWrite(leftM_In2,HIGH);
  }
  analogWrite(leftM_PWM,abs(left));
  analogWrite(rightM_PWM,abs(right));
  delay(udelay);
}
//////////////////////////////////////////
void mStop() {
  digitalWrite(rightM_In1,HIGH);
  digitalWrite(rightM_In2,HIGH);
  digitalWrite(leftM_In1,HIGH);
  digitalWrite(leftM_In2,HIGH);
  analogWrite(leftM_PWM,0);
  analogWrite(rightM_PWM,0);
  delay(100);
}
//////////////////////////////////////////
