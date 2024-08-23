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

int pinGate = 14;

BLYNK_WRITE(V2){
    if(param.asInt()==1){
        Serial.println("Gate Opened");
        digitalWrite(pinGate, LOW);
        delay(500);
        digitalWrite(pinGate, HIGH);
    }else{
        Serial.println("Gate Closed");
    }
}


BLYNK_CONNECTED(){
  Blynk.syncVirtual(V2);
}

void setup()
{
  // Debug console
  Serial.begin(115200);
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
  pinMode(pinGate, OUTPUT);
}

void loop()
{
  Blynk.run();
}

