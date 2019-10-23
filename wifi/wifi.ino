#include <SDS011.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

float p10, p25;
int error;

SDS011 my_sds;


 
void setup() {
  my_sds.begin(D2, D1); //Connect RX to D1, Connect TX to D2
  Serial.begin(9600);   
  Serial.println("Waiting");
 //Serial connection
//  WiFi.begin("CHARLOTTE 1", "0987654321"); 
  WiFi.begin("Lormz", "aaaaaaaa");  //WiFi connection
 
  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
 
}
 
void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    Serial.println("connected");
    HTTPClient http;    //Declare object of class HTTPClient

    error = my_sds.read(&p25, &p10);
    Serial.println(p25);
    Serial.println(p10);
    Serial.println(error);
    if (!error) {
    Serial.println("P2.5: " + String(p25));
    Serial.println("P10:  " + String(p10));
    }
    delay(100);
 
    http.begin("http://192.168.43.54:5000/postdata");      //Specify request destination
    http.addHeader("Content-Type", "text/plain");  //Specify content-type header
    

    int httpCode = http.POST(String(p25) + "," + String(p10));   //Send the request
    String payload = http.getString();                                        //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload + "pay");    //Print request response payload
 
    http.end();  //Close connection
 
  } else {
 
    Serial.println("Error in WiFi connection");
 
  }
 
  delay(30000);  //Send a request every 30 seconds
 
}
