# ESP32-PC-MQTT-communication
This project demonstrates two-way communication between an ESP32 microcontroller and a PC or a Rasberry Pi or any other device capable of running python programs using the MQTT messaging protocol. 
It provides a basic framework for building applications that exchange data between these devices.

# Features:
-Connects ESP32 to a WiFi network.

-Establishes connection with an MQTT broker.

-Subscribes to a shared topic for message exchange.

-Sends messages from ESP32 to PC (example: current time).

-Receives messages from PC to ESP32 (example: greetings).

-Uses FreeRTOS tasks for concurrent message sending and receiving (optional).

-Provides comments and explanations for code clarity.

# Getting Started:

1.Replace the WiFi credentials (ssid and password) in the ESP32 code with your network details.
2.Update the MQTT broker address (mqtt_broker), port (mqtt_port), and topic (mqtt_topic) in both ESP32 and PC code to match your setup.
3.Ensure the PC program (using paho-mqtt) is running and subscribed to the same topic.
4.Upload the ESP32 code to your device using the Arduino IDE or a similar tool.

# NOTE :
By in the given code, BOTH esp32 and python program sends a greeting msg (HELLO FROM ESP/PC ) with timestamp. u can remove it and create according to ur needs:

# HOW TO MODIFY PYTHON CODE FOR UR NEEDS:
# To send data:
*In the main function, modify the "send_message()" function call to accept user input for the message. Here's an example:*

def main(queue):
    while True:
        message = input("Enter message to send: ")  # Get user input
        send_message(message)  # Pass user input to send_message function
        # ... rest of your code


# To Recive data:
The current code already uses get_latest_message(queue) to capture the latest message received from the ESP32. You can modify how you handle the received data (e.g., print it, store it in a list).

# HOW TO MODIFY ESP32 CODE FOR UR NEEDS:
# To send data:
simply use send_msg() function on void loop() to send data. Here is an eg:
def void loop(){
  send_msg("HELLO FROM ESP32")
 .......rest of ur logic here

# To recive data:
The current code already uses the mqttCallback function to handle received messages. You can access the received message data using the global variable "last_received_msg"
 in this code, it only holds last recived msg in the variable, u can add ur logic to hold multiple datas by storing in a list etc...
 
