int num = 12;

char incomingByte;
bool send;

const int program_size = 2048;
char instructions[program_size];
void setup() {
  Serial.begin(9600);
}

void loop() {
  for(int i = 0;i < program_size;i++){
    send =
    while(send){
      if (Serial.available() > 0) {
        // read the incoming byte:
        incomingByte = Serial.read();
        instructions[i] = incomingByte;
        // say what you got:
        Serial.print("I received: ");
        Serial.println(incomingByte);
        send = false;
    }
    }
  }

}