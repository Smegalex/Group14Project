from microbit import *
import radio
# Connect server to PC

### Notes ###

# All kitroniks with have my personal ID to send to, prob use time.sleep to avoid sending at the same time
# Randomised sleep can be used to help stop collisions

# Dictionary to store the latest data from each sensor
def receiveCommand(serverId: str):
    while True:
        message = radio.receive()# Check for incoming messages

        if message:
            try: eval(message)
            except: return 0
            if not message.endswith("\n"):  
                message += "\n"
            uart.write(message)
