int BASE = 2 ;  // the I/O pin for the first LED
int NUM = 6;   // number of LEDs

int inpin=8;
int val;
int Delay=100;

void setup()
{
  Serial.begin(9600);
   for (int i = BASE; i < BASE + NUM; i ++) 
   {
     pinMode(i, OUTPUT);   // set I/O pins as output
   }
   pinMode(inpin, INPUT);
}

void loop()
{
  for(int i = BASE; i < BASE + NUM; i ++)
  {
    val=digitalRead(inpin);
      digitalWrite(i, HIGH);
      delay(Delay);
      digitalWrite(i - 1, LOW);
      
      if(val==HIGH && i==BASE)
      {
           for (int i = BASE; i < BASE + NUM; i ++) 
           {
             digitalWrite(i, HIGH);    // set I/O pins as “low”, turn off LEDs one by one.
             delay(200);        // delay
           }
           for (int i = BASE; i < BASE + NUM; i ++) 
           {
             digitalWrite(i, LOW);    // set I/O pins as “high”, turn on LEDs one by one
             delay(200);        // delay
           } 
      }
      if(val==HIGH && i != BASE)
      {
        for(int n=BASE;n < BASE + NUM;n++){
          digitalWrite(n, HIGH);
        }
        delay(1000);
        for(int n=BASE;n < BASE + NUM;n++){
          digitalWrite(n, LOW);
        }
      }
  }
  digitalWrite(BASE + NUM - 1, LOW);
  
}
