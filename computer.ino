 int Base = 2;
 int out = 3;
 int in = 4;


void setup() {
  Serial.begin(9600);

  for(int i = 0; i < out;i++){
    pinMode(Base+i, OUTPUT);
  }
  for(int i = 0; i < in;i++){
    pinMode(Base+i+out,INPUT);
  }

}

void loop() {
  for(int i = 0; i < out;i++){
    digitalWrite(Base+i, HIGH);
    for(int j = 0; j < in;j++){
      if(digitalRead(Base+j+out)){
        Serial.print(j);
      }
    digitalWrite(Base+i, LOW);
    }
  }

}
