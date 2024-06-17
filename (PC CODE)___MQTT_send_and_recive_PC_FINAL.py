from multiprocessing import Process, Queue  # Import Queue here
import paho.mqtt.client as mqtt
import time
from datetime import datetime
from queue import Empty  # Import Empty exception from queue module

broker = "broker.emqx.io"
port = 1883
topic = "emqx/esp32"  # Same topic for both sending and receiving


def current_time():
    return datetime.now().strftime("%H:%M:%S")

# Example usage
print(current_time())

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to {broker} with result code {rc}")
        client.subscribe(topic, qos=0)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    received_msg = msg.payload.decode()
    if received_msg.startswith("ESP32:"):
        received_msg = received_msg[6:]  # Strip the prefix
        userdata.put(received_msg)  # Put message into queue using userdata

def receive_msg(queue):
    client = mqtt.Client(userdata=queue)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(broker, port, 60)
        client.loop_forever()
    except Exception as e:
        print(f"Error connecting to MQTT broker: {e}")

def send_message(message):
    prefixed_message = f"{message}"  # Add a space for readability
    client = mqtt.Client()
    try:
        client.connect(broker, port, 60)
        # Ensure you publish to 'topic', not 'prefixed_message'
        client.publish(topic, prefixed_message)
        print(f"Sent message: {prefixed_message}\n")
    except Exception as e:
        print(f"Error connecting to MQTT broker: {e}")

def get_latest_message(queue):
    try:
        return queue.get_nowait()  # Non-blocking get
    except Empty:  # Use Empty exception from queue module
        return None  # Return None if no message is availab

def main(queue):
    while True:
        send_message(f"PC: Hello from PC {current_time()}")
        
        time.sleep(10)
        
        latest_message = get_latest_message(queue)  # Use helper function to get latest message
        if latest_message:
            print(f"Received message: {latest_message}\n")

        time.sleep(10)

if __name__ == '__main__':
    queue = Queue()  # Create a queue object
    receive_process = Process(target=receive_msg, args=(queue,))  # Pass queue as an argument
    
    receive_process.start()  # Start the receiving process

    main(queue)  # Pass queue to main

    receive_process.join()  # Wait for the receiving process to finish