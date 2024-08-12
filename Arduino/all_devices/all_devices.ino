#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <time.h>
#include <SoftwareSerial.h>
#include <EEPROM.h>

int light_add = 0;
int fan_add = 0;
byte light;
byte fan;

const char* ssid     = "WiFi Name";
const char* password = "WiFi Password";
ESP8266WebServer server(80);

int pinTube = 14;
int pinFan = 5;

void setup() {
  Serial.begin(9600);
  EEPROM.begin(512);
  
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  //pinMode(LED_BUILTIN, OUTPUT);
  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }
  server.on("/on_tube", handleONTube);
  server.on("/off_tube", handleOFFTube);
  server.on("/on_fan", handleONFan);
  server.on("/off_fan", handleOFFFan);
  server.on("/offall", handleOFF);
  server.on("/light", light_value);
  server.on("/fan", fan_value);
  server.on("/home", home_page);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
  pinMode(pinTube, OUTPUT);
  pinMode(pinFan, OUTPUT);
}

void loop() {
  server.handleClient();
  MDNS.update();
  EEPROM.write(light_add, light);
  EEPROM.write(fan_add, fan);
  light = EEPROM.read(light_add);
  fan = EEPROM.read(fan_add);
  if(light) handleONTube;
  else handleOFFTube;
  if(fan) handleONFan;
  else handleOFFFan;
}

void light_value() {
  if (EEPROM.read(light_add)) server.send(200, "text/plain", "light on");
  else server.send(200, "text/plain", "light off");
}

void fan_value() {
  if (EEPROM.read(fan_add)) server.send(200, "text/plain", "fan on");
  else server.send(200, "text/plain", "fan off");
}

void handleONTube() {
  digitalWrite(pinTube, LOW);
  server.send(200, "text/plain", "light_on\r\n");
  light = 1;
}

void handleOFFTube() {
  digitalWrite(pinTube, HIGH);
  server.send(200, "text/plain", "light_off\r\n");
  light = 0;
}

void handleONFan() {
  digitalWrite(pinFan, LOW);
  server.send(200, "text/plain", "fan_on\r\n");
  fan = 1;
}

void handleOFFFan() {
  digitalWrite(pinFan, HIGH);
  server.send(200, "text/plain", "fan_off\r\n");
  fan = 0;
}

void handleOFF() {
  digitalWrite(pinTube, HIGH);
  digitalWrite(pinFan, HIGH);
  server.send(200, "text/plain", "All devices off\r\n");
  fan = 0;
  light = 0;
}

void home_page(){
  String ip_address = WiFi.localIP().toString();
  String html_text = "<!DOCTYPE html>"
    "<html lang='en'>"
    "<head>"
        "<meta charset='UTF-8'>"
        "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        "<title>Devices Control System</title>"
    "</head>"
    "<body style='background-image:linear-gradient(to right, yellow, red,rgb(114, 236, 114), blue); align-items:center; text-align:center; margin: 0 auto;'>"
        "<div style='margin:2rem; text-align:center; align-items:center;'>"
            "<h1 style='border:2px solid black; margin: 2rem 4rem; padding: 2rem 4rem; border-radius:20px; font-size:5rem;'>Devices Control Page</h1>"
            "<div style='border:2px solid black; margin: 2rem 4rem; padding: 2rem 4rem; border-radius:20px;'>"
                "<div style='margin: 2rem 4rem;'>"
                    "<button style='padding:1rem 2rem; margin:1rem 2rem; border-radius: 10px; font-size:1.5rem; font-weight:bold; background-image:linear-gradient(to right, rgb(0, 255, 255), orange);' id='light1 on'> Main Light On</button>"
                    "<button style='padding:1rem 2rem; margin:1rem 2rem; border-radius: 10px; font-size:1.5rem; font-weight:bold; background-image:linear-gradient(to right, rgb(0, 255, 255), orange);' id='light1 off'>Main Light Off</button>"
                "</div>"
                "<div style='margin: 2rem 4rem;'>"
                    "<button style='padding:1rem 2rem; margin:1rem 2rem; border-radius: 10px; font-size:1.5rem; font-weight:bold; background-image:linear-gradient(to right, rgb(0, 255, 255), orange);' id='fan on'>Fan On</button>"
                    "<button style='padding:1rem 2rem; margin:1rem 2rem; border-radius: 10px; font-size:1.5rem; font-weight:bold; background-image:linear-gradient(to right, rgb(0, 255, 255), orange);' id='fan off'>Fan Off</button>"
                "</div>"
                "<div style='margin: 2rem 4rem;'>"
                    "<button style='padding:1rem 2rem; margin:1rem 2rem; border-radius: 10px; font-size:1.5rem; font-weight:bold; background-image:linear-gradient(to right, rgb(0, 255, 255), orange);' id='All Device Off'>All devices off</button>"
                "</div>"
            "</div>"
        "</div>"
        "<script>"
            "const light1_on = document.getElementById('light1 on');"
            "const light1_off = document.getElementById('light1 off');"
            "const fan_on = document.getElementById('fan on');"
            "const fan_off = document.getElementById('fan off');"
            "const all_off = document.getElementById('All Device Off');"
            "light1_on.addEventListener('click', () => { fetch('http://" + ip_address + "/on_tube')});"
            "light1_off.addEventListener('click',() => { fetch('http://" + ip_address + "/off_tube')});"
            "fan_on.addEventListener('click', () => { fetch('http://" + ip_address + "/on_fan')});"
            "fan_off.addEventListener('click', () => { fetch('http://" + ip_address + "/off_fan')});"
            "all_off.addEventListener('click', () => { fetch('http://" + ip_address + "/offall')});"
        "</script>"
    "</body>"
    "</html>";
  server.send(200, "text/html", html_text);
}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

