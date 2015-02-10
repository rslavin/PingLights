#define RED 9
#define YELLOW 10
#define GREEN 11


void setup() {
  Serial.begin(115200);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

}
char inByte = '\0';
void loop() {
  delay(1000);
  
  if(Serial.available()){
    inByte = Serial.read();
  }
  switch(inByte) {
    case '1': // good
      greenOnly();
      break;
    case '2': // med
      yellowOnly();
      break;
    case '3': // bad
      redOnly();
      break;
    case '4': // timeout (blinks)
      allOff();
      delay(500);
      redOnly();
      delay(500);
      break;
    default:
      allOff();
  }
}
  void redOnly(){
    digitalWrite(RED, HIGH);
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, LOW);
  }
  
  void redBlink(){
      allOff();
      delay(500);
      redOnly();
      delay(500);
  }
  
  void greenOnly(){
    digitalWrite(RED, LOW);
    digitalWrite(GREEN,HIGH);
    digitalWrite(YELLOW, LOW);
  }
  
  void yellowOnly(){
    digitalWrite(RED, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, HIGH);
  }
  
  void allOn(){
    digitalWrite(RED, HIGH);
    digitalWrite(GREEN, HIGH);
    digitalWrite(YELLOW, HIGH);
  }
  
  void allOff(){
    digitalWrite(RED, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, LOW);
  }
