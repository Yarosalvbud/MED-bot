#include <Servo.h> // подключаем библиотеку для работы с сервоприводом

int SERVO = 12;
int URECHO = 2;
int URTRIG = 3;
unsigned int DistanceMeasured = 0;
int ACTUAL_POSITION = 90;


Servo servo1;

void setup() {
  Serial.begin(115200);
  servo1.attach(12); // привязываем сервопривод к аналоговому выходу 10
  servo1.write(ACTUAL_POSITION);
  pinMode(URTRIG, OUTPUT);
  digitalWrite(URTRIG, HIGH);
  pinMode(URECHO, INPUT);
  delay(500);

}

void loop() {

  if (Serial.available() > 0) {
    auto value = Serial.parseInt();
    if (value != 0) {
      
      servo1.write(ACTUAL_POSITION - value);
        if (ACTUAL_POSITION - value > 48){
      ACTUAL_POSITION = ACTUAL_POSITION - value;
        }
    }

  }
  digitalWrite(URTRIG, LOW);
  digitalWrite(URTRIG, HIGH);

  unsigned long LowLevelTime = pulseIn(URECHO, LOW) ;
  DistanceMeasured = LowLevelTime / 50;  // every 50us low level stands for 1cm
  Serial.println(DistanceMeasured);
}
