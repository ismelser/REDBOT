const char buzzer = 9;
const char button = 12;
const char leftM_In1 = 2;
const char leftM_In2 = 4;
const char leftM_PWM = 5;
const char rightM_In1 = 7;
const char rightM_In2 = 8;
const char rightM_PWM = 6;
const char rightW = A5;
const char leftW = A4;
const char encodeL = A2;
const char encodeR = 10;
const char servo = A1;
//////////////////////////////////////////
void setup() {
  Serial.begin(9600);
  interrupts();


  pinMode(button, INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);

  pinMode(leftM_In1, OUTPUT);
  pinMode(leftM_In2, OUTPUT);
  pinMode(leftM_PWM, OUTPUT);
  pinMode(rightM_In1, OUTPUT);
  pinMode(rightM_In2, OUTPUT);
  pinMode(rightM_PWM, OUTPUT);

  pinMode(rightW, INPUT);
  pinMode(leftW, INPUT);
  pinMode(encodeR, INPUT_PULLUP);
  pinMode(encodeL, INPUT_PULLUP);
  pinMode(servo, OUTPUT);

  initU();
}
void initU() {
  tone(buzzer, 440);
  delay(50);
  tone(buzzer, 880);
  delay(100);
  noTone(buzzer);
  delay(100);
}

void loop() {
  while (digitalRead(button)==HIGH) {}
  delay(1000);
  while (digitalRead(button)==HIGH) {
    forwardUnbound();
    if (digitalRead(rightW)==LOW || digitalRead(leftW)==LOW) {
      backward(1,255);
      turn(1,255);
    }
  }
}

void forward(float turns, int value) {
  digitalWrite(rightM_In1, LOW);
  digitalWrite(rightM_In2, HIGH);
  digitalWrite(leftM_In1, HIGH);
  digitalWrite(leftM_In2, LOW);
  analogWrite(leftM_PWM, abs(value));
  analogWrite(rightM_PWM, abs(value));
  int count = 0;
  int previous = 0;
  int current = 0;
  current = digitalRead(10);
  while (count < turns * 192) {
    previous = current;
    current = digitalRead(10);
    if (!current && previous) {
      count++;
    }
    if ((turns * 192) - count < 10) {
      digitalWrite(rightM_In1, HIGH);
      digitalWrite(rightM_In2, LOW);
      digitalWrite(leftM_In1, LOW);
      digitalWrite(leftM_In2, HIGH);
      analogWrite(leftM_PWM, abs(value));
      analogWrite(rightM_PWM, abs(value));
    }

  }
  mStop();
}

void forwardUnbound() {
  digitalWrite(rightM_In1, LOW);
  digitalWrite(rightM_In2, HIGH);
  digitalWrite(leftM_In1, HIGH);
  digitalWrite(leftM_In2, LOW);
  analogWrite(leftM_PWM, abs(255));
  analogWrite(rightM_PWM, abs(255));
}

void backward(float turns, int value) {
  digitalWrite(rightM_In1, HIGH);
  digitalWrite(rightM_In2, LOW);
  digitalWrite(leftM_In1, LOW);
  digitalWrite(leftM_In2, HIGH);
  analogWrite(leftM_PWM, abs(value));
  analogWrite(rightM_PWM, abs(value));
  int count = 0;
  int previous = 0;
  int current = 0;
  current = digitalRead(10);
  while (count < turns * 192) {
    previous = current;
    current = digitalRead(10);
    if (!current && previous) {
      count++;
    }
    if ((turns * 192) - count < 10) {
      digitalWrite(rightM_In1, LOW);
      digitalWrite(rightM_In2, HIGH);
      digitalWrite(leftM_In1, HIGH);
      digitalWrite(leftM_In2, LOW);
      analogWrite(leftM_PWM, abs(value));
      analogWrite(rightM_PWM, abs(value));
    }

  }
  mStop();
}

void turn(float turns, int value) {
  digitalWrite(rightM_In1, HIGH);
  digitalWrite(rightM_In2, LOW);
  digitalWrite(leftM_In1, HIGH);
  digitalWrite(leftM_In2, LOW);
  analogWrite(leftM_PWM, abs(value));
  analogWrite(rightM_PWM, abs(value));
  int count = 0;
  int previous = 0;
  int current = 0;
  current = digitalRead(10);
  while (count < turns * 192) {
    previous = current;
    current = digitalRead(10);
    if (!current && previous) {
      count++;
    }
    if ((turns * 192) - count < 30) {
      digitalWrite(rightM_In1, HIGH);
      digitalWrite(rightM_In2, LOW);
      digitalWrite(leftM_In1, LOW);
      digitalWrite(leftM_In2, HIGH);
      analogWrite(leftM_PWM, abs(value));
      analogWrite(rightM_PWM, abs(value));
    }

  }
  mStop();
}

void mStop() {
  digitalWrite(rightM_In1, HIGH);
  digitalWrite(rightM_In2, HIGH);
  digitalWrite(leftM_In1, HIGH);
  digitalWrite(leftM_In2, HIGH);

  analogWrite(leftM_PWM, 0);
  analogWrite(rightM_PWM, 0);
  delay(100);

}


