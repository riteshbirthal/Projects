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
#define BLYNK_TEMPLATE_NAME         "BLYNK_TEMLATE_NAME"
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

BLYNK_WRITE(V0){
  HTTPClient http;
  WiFiClient client;
  if(param.asInt()==1){
    Serial.println("Fan ON");
    http.begin(client, "http://192.168.1.5/on_fan");
    int httpCode = http.GET();
    http.end();
  }else{
    Serial.println("Fan OFF");
    http.begin(client, "http://192.168.1.5/off_fan");
    int httpCode = http.GET();
    http.end();
  }
}

BLYNK_WRITE(V1){
  HTTPClient http;
  WiFiClient client;
  if(param.asInt()==1){
    Serial.println("Light ON");
    http.begin(client, "http://192.168.1.5/on_tube");
    int httpCode = http.GET();
    http.end();
  }else{
    Serial.println("Light OFF");
    http.begin(client, "http://192.168.1.5/off_tube");
    int httpCode = http.GET();
    http.end();
  }
}


BLYNK_WRITE(V2){
  HTTPClient http;
  WiFiClient client;
  if(param.asInt()==1){
    Serial.println("Gate Opened");
    http.begin(client, "http://192.168.1.6/open_gate");
    int httpCode = http.GET();
    http.end();
  }else{
    Serial.println("Gate Closed");
  }
}


BLYNK_CONNECTED(){
  Blynk.syncVirtual(V0);
}

void setup()
{
  // Debug console
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop()
{
  Blynk.run();
}


