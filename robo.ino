#include <Servo.h> // подключаем библиотеку для работы с сервоприводом

int SERVO = 12;
int URECHO = 2;
int URTRIG = 3;
unsigned int DistanceMeasured = 0;



Servo servo1;

void setup() {
  Serial.begin(9600);
  servo1.attach(12); // привязываем сервопривод к аналоговому выходу 10
  servo1.write(90);
  pinMode(URTRIG, OUTPUT);
  digitalWrite(URTRIG, HIGH);
  pinMode(URECHO, INPUT);
  delay(500);

}

void loop() {
  if (Serial.available() > 0) {
    auto value = Serial.parseInt();
    if (value != 0) {
      servo1.write(value);
      Serial.println(value);
    }

  }
  digitalWrite(URTRIG, LOW);
  digitalWrite(URTRIG, HIGH);

  unsigned long LowLevelTime = pulseIn(URECHO, LOW) ;
  DistanceMeasured = LowLevelTime / 50;  // every 50us low level stands for 1cm
  Serial.println(DistanceMeasured);

  delay(200);
}