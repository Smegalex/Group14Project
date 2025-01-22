from microbit import *
import radio
# Connect server to PC

personal_id = "server14C"# ID for controller

radio.on()# Turn on the radio
radio.config(channel=14, group=1)# Set the channel

### Notes ###
# If message starts with certain ID, then display.scroll to test

# All kitroniks with have my personal ID to send to, prob use time.sleep to avoid sending at the same time
# Randomised sleep can be used to help stop collisions

# Dictionary to store the latest data from each sensor
sensor_data = {}

while True:
    message = radio.receive()# Check for incoming messages
    if message:
        # Parse the message for the sender ID
        if message.startswith("Kitronik1:"):
            display.scroll("From K1: " + message[9:])  # Handle Kitronik 1
            sensor_data.append

        elif message.startswith("Kitronik2:"):
            display.scroll("From K2: " + message[9:])  # Handle Kitronik 2
            sensor_data.append

        elif message.startswith("Kitronik3:"):
            display.scroll("From K3: " + message[9:])  # Handle Kitronik 3
            sensor_data.append

        elif message.startswith("Kitronik4:"):
            display.scroll("From K4: " + message[9:])  # Handle Kitronik 4
            sensor_data.append

        else:
            display.scroll("Unknown: " + message)  # Handle unknown messages
