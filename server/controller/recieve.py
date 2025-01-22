from microbit import *
import radio
# Connect server to PC

personal_id = "Controller"

radio.on()# Turn on the radio
radio.config(channel=14, group=1)# Set the channel

while True:
    message = radio.receive()# Check for incoming messages
    if message:
        # Parse the message for the sender ID
        if message.startswith("Kitronik1:"):
            display.scroll("From K1: " + message[9:])  # Handle Kitronik 1

        elif message.startswith("Kitronik2:"):
            display.scroll("From K2: " + message[9:])  # Handle Kitronik 2

        elif message.startswith("Kitronik3:"):
            display.scroll("From K3: " + message[9:])  # Handle Kitronik 3

        elif message.startswith("Kitronik4:"):
            display.scroll("From K4: " + message[9:])  # Handle Kitronik 4

        else:
            display.scroll("Unknown: " + message)  # Handle unknown messages
