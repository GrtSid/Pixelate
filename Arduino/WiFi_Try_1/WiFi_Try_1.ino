#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <String.h>

int speedCar = 150;     // 50 - 255.
const char* ssid = "Windows&7";
const char* password = "ThroughM";

const char* host = "192.168.173.1";
String url = "/MyCodes/pixelate.txt";
char r;
int len;
void setup() {
  Serial.begin(115200); // Initialize serial communication at 9600 bits per second
  Serial.printf("Connecting to %s ",ssid);
  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");
  
  // Set pins as outputs
  pinMode(0, HIGH);    //FR +
  pinMode(2, HIGH);    //FL +
  pinMode(16, OUTPUT);//pinMode(1, OUTPUT);  //FR -
  pinMode(14, OUTPUT);//pinMode(3, OUTPUT);  //FL -
  pinMode(4, OUTPUT);  //LED1 +
  pinMode(5, OUTPUT);  //LED1 -
  pinMode(12, OUTPUT);//pinMode(6, OUTPUT);  //LED2 +
  pinMode(13, OUTPUT);//pinMode(7, OUTPUT);  //LED2 -
  pinMode(15, OUTPUT);//pinMode(8, OUTPUT);
  pinMode(2, OUTPUT);//pinMode(9, OUTPUT);
 }
void loop() {
  WiFiClient client;
  if(client.connect(host,80))
  {
    client.print(String("GET /") + url + " HTTP/1.1\r\n" +
                 "Host: " + host + "\r\n" +
                 "Connection: close\r\n" +
                 "\r\n"
                );
    while (client.connected())
    {
      if (client.available())
      {
        String line = client.readStringUntil('\n');
        //Serial.println(line);
        len=line.length();
        for(int i=0 ; i<6 ; i++){
          r=line[i];
          Serial.println(r);
          switch (r) {
            case 'f':  //Moving the Car Forward,,f=1
              digitalWrite(16, HIGH);
              digitalWrite(14, LOW);
              digitalWrite(4, HIGH);
              digitalWrite(5, LOW);
              digitalWrite(12, HIGH);
              digitalWrite(13, LOW);
              digitalWrite(15, LOW);
              digitalWrite(2, LOW);
              delay(2500);
              digitalWrite(16, LOW);
              digitalWrite(14, LOW);
              Serial.println("FORWARD AND LED1 IS ON");
              break;
            case 'l':  //Moving the Car Left,,l=3
              digitalWrite(16, HIGH);
              digitalWrite(14, LOW);
              digitalWrite(4, LOW);
              digitalWrite(5, LOW);
              digitalWrite(12, HIGH);
              digitalWrite(13, LOW);
              digitalWrite(15, LOW);
              digitalWrite(2, LOW);
              delay(4000);
              digitalWrite(4, HIGH);
              delay(2500);
              digitalWrite(16, LOW);
              digitalWrite(4, LOW);
              Serial.println("LEFT AND LED1 IS ON");
              break;
            case 'r':   //Moving the Car Right,,r=2
              digitalWrite(16, LOW);
              digitalWrite(14, HIGH);
              digitalWrite(4, LOW);
              digitalWrite(5, LOW);
              digitalWrite(12, HIGH);
              digitalWrite(13, LOW);
              digitalWrite(15, LOW);
              digitalWrite(2, LOW);
              delay(4000);
              digitalWrite(4,HIGH);
              delay(2500);
              digitalWrite(4, LOW);
              digitalWrite(16, LOW);
              Serial.println("RIGHT AND LED1 IS ON");
              break;
	    case'a':
		digitalWrite(16, LOW);
              digitalWrite(14, LOW);
              digitalWrite(4, LOW);
              digitalWrite(5, LOW);
              digitalWrite(12, LOW);
              digitalWrite(13, LOW);
              digitalWrite(15, HIGH);
              digitalWrite(2, LOW);
            default:
              digitalWrite(15, LOW);
              digitalWrite(16, LOW);
              digitalWrite(2, LOW);
              digitalWrite(14, LOW);
              digitalWrite(4, LOW); 
              digitalWrite(5, LOW);
              digitalWrite(12, LOW);
              digitalWrite(13, LOW);
              Serial.println("STOP AND LED2 IS ON AND LED1 OS OFF");
           }
        }
      }
    }
    client.stop();
  }
  else
  {
    Serial.println("connection failed!]");
    client.stop();
  }
  }
