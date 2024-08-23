/*************************************************************

  You’ll need:
   - Blynk IoT app (download from App Store or Google Play)
   - ESP8266 board
   - Decide how to connect to Blynk
     (USB, Ethernet, Wi-Fi, Bluetooth, ...)

  There is a bunch of great example sketches included to show you how to get
  started. Think of them as LEGO bricks  and combine them as you wish.
  For example, take the Ethernet Shield sketch and combine it with the
  Servo example, or choose a USB sketch and add a code from SendData
  example.
 *************************************************************/

/* Fill-in information from Blynk Device Info here */
#define BLYNK_TEMPLATE_ID           "BLYNK_TEMPLATE_ID"
#define BLYNK_TEMPLATE_NAME         "BLYNK_TEMPLATE_NAME"
#define BLYNK_AUTH_TOKEN            "BLYNK_AUTH_TOKEN"
/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <ESP8266HTTPClient.h>

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "WiFi Name";
char pass[] = "WiFi Password";

int pinLight = 4;
int pinFan = 5;

BLYNK_WRITE(V0){
    if(param.asInt()==1){
        Serial.println("Fan ON");
        digitalWrite(pinFan, LOW);
    }else{
        Serial.println("Fan OFF");
        digitalWrite(pinFan, HIGH);
    }
}

BLYNK_WRITE(V1){
    if(param.asInt()==1){
        Serial.println("Light ON");
        digitalWrite(pinLight, LOW);
    }else{
        Serial.println("Light OFF");
        digitalWrite(pinLight, HIGH);
    }
}


BLYNK_CONNECTED(){
  Blynk.syncVirtual(V0);
  Blynk.syncVirtual(V1);
}

void setup()
{
  // Debug console
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  pinMode(pinLight, OUTPUT);
  pinMode(pinFan, OUTPUT);

}

void loop()
{
  Blynk.run();
}

