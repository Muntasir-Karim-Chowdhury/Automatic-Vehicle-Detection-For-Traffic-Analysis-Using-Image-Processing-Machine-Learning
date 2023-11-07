int value=0;
const int green=8;
const int red=9;
const int yellow=10;

void setup(){
  
  Serial.begin(9600);
  pinMode(green,OUTPUT);
  digitalWrite(green,LOW);
  pinMode(red,OUTPUT);
  digitalWrite(red,LOW);
  pinMode(yellow,OUTPUT);
  digitalWrite(yellow,LOW);
  //Serial.println("connection established....");
  }

void loop(){
  while(Serial.available())
    {
      value=Serial.read();
      //Serial.print(serialData);
    }
    
    if(value=='0'){
      digitalWrite(green,HIGH);}
    else if(value=='1'){
      digitalWrite(green,LOW);
      digitalWrite(yellow,HIGH);}
    else if(value=='2'){
      digitalWrite(yellow,LOW);
      digitalWrite(red,HIGH);}
    }

