from microbit import *
import radio
# Connect server to PC

radio.on()               # Turn on the radio
radio.config(channel=14, group=1)  # Set the channel

while True:
    message = radio.receive()  # Check for incoming messages
    if message:
        display.scroll("Recieved",message)  # Display the message on the micro:bit

