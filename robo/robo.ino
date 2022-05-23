#define SPEED_LEFT 6
#include <Servo.h> // подключаем библиотеку для работы с сервоприводом
int SERVO = 12;
#define SPEED_RIGHT 5
#define DIR_LEFT 7
#define DIR_RIGHT 4
#include <time.h>
#include <SoftwareSerial.h>
Servo servo1;
SoftwareSerial Serial1(11, 10); //Serial1 connected to TOF Serial：10<-->RX, 11<-->TX

unsigned char TOF_data[32] = {0};   //store 2 TOF frames
unsigned char TOF_length = 16;
unsigned char TOF_header[3] {0x57, 0x00, 0xFF};
unsigned long TOF_system_time = 0;
unsigned long TOF_distance = 0;
unsigned char TOF_status = 0;
unsigned int TOF_signal = 0;
unsigned char TOF_check = 0;
unsigned long LowLevelTime;
unsigned int DistanceMeasured = 0;
int ACTUAL_POSITION = 90;



void setup() {
  Serial.begin(115200);
  servo1.attach(12);

  for (int i = 4; i <= 7; ++i)
    pinMode(i, OUTPUT);
  // initialize both serial ports:
  Serial.begin(115200);
  Serial1.begin(115200);
}

bool verifyCheckSum(unsigned char data[], unsigned char len) {
  TOF_check = 0;

  for (int k = 0; k < len - 1; k++)
  {
    TOF_check += data[k];
  }

  if (TOF_check == data[len - 1])
  {
    return true;
  } else {
    return false;
  }

}

int get_santimetr() {
  if (Serial1.available() >= 32) {
    for (int i = 0; i < 32; i++)
    {
      TOF_data[i] = Serial1.read();
    }

    for (int j = 0; j < 16; j++)
    {
      if ( (TOF_data[j] == TOF_header[0] && TOF_data[j + 1] == TOF_header[1] && TOF_data[j + 2] == TOF_header[2]) && (verifyCheckSum(&TOF_data[j], TOF_length)))
      {
        if (((TOF_data[j + 12]) | (TOF_data[j + 13] << 8) ) == 0)
        {
        } else {
          TOF_distance = (TOF_data[j + 8]) | (TOF_data[j + 9] << 8) | (TOF_data[j + 10] << 16);
          Serial.println(TOF_distance / 10);
          return TOF_distance;

        }
        break;
      }
    }
    Serial.println(0);
    return 0;

  }
}

void loop() {
  while (true) {
    LowLevelTime = get_santimetr();

    if (LowLevelTime <= 500) {
      analogWrite(SPEED_LEFT, 0);
      analogWrite(SPEED_RIGHT, 0);


      break;

    }

    analogWrite(SPEED_RIGHT, 60);
    digitalWrite(DIR_RIGHT, LOW);
    analogWrite(SPEED_LEFT, 60);
    digitalWrite(DIR_LEFT, LOW);

  }
  if (Serial.available() > 0) {
    auto value = Serial.parseInt();
    if (value <= -20) {
      analogWrite(SPEED_RIGHT, 60);
      digitalWrite(DIR_RIGHT, LOW);
      analogWrite(SPEED_LEFT, 60);
      digitalWrite(DIR_LEFT, HIGH);
      delay(2.5 * value);
      analogWrite(SPEED_LEFT, 0);
      analogWrite(SPEED_RIGHT, 0);
    }
    if (value >= 20) {
      analogWrite(SPEED_RIGHT, 60);
      digitalWrite(DIR_RIGHT, HIGH);
      analogWrite(SPEED_LEFT, 60);
      digitalWrite(DIR_LEFT, LOW);
      delay(2.5 * value);
      analogWrite(SPEED_LEFT, 0);
      analogWrite(SPEED_RIGHT, 0);
    }


  }



}
