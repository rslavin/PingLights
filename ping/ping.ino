boolean ON = LOW;
boolean OFF = HIGH;

boolean RED[] = {ON, OFF, OFF};
boolean GREEN[] = {OFF, ON, OFF};
boolean BLUE[] = {OFF, OFF, ON};
boolean YELLOW[] = {ON, ON, OFF};
boolean CYAN[] = {OFF, ON, ON};
boolean MAGENTA[] = {ON, OFF, ON};
boolean WHITE[] = {ON, ON, ON};
boolean BLACK[] = {OFF, OFF, OFF};

boolean* COLORS[] = {RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK};

int DIGITAL_OUTS[] = {9, 10, 11};

char inByte = '\0';
int lastRead = 0;

void setColor(boolean* color){
  for(int i = 0; i < 3; i++){
    digitalWrite(DIGITAL_OUTS[i], color[i]);
  }
}


void setup() {
  Serial.begin(115200);
  for(int i = 0; i < 3; i++){
    pinMode(DIGITAL_OUTS[i], OUTPUT);
  }
  setColor(BLACK);
}

void loop() {
  delay(1000);
  
  if(Serial.available()){
    inByte = Serial.read();
    lastRead = 0;
  }
  if(lastRead < 15){
    switch(inByte) {
      case '1': // good
        setColor(GREEN);
        break;
      case '2': // med
        setColor(YELLOW);
        break;
      case '3': // bad
        setColor(RED);
        break;
      case '4': // timeout (blinks)
        setColor(BLACK);
        delay(500);
        setColor(RED);
        delay(500);
        break;
      case '5': // intermittent (blinks)
        setColor(BLACK);
        delay(500);
        setColor(YELLOW);
        delay(500);
        break;
      default:
        setColor(BLACK);
    }
  }else{
    setColor(BLACK);
  }
  lastRead++;
}
