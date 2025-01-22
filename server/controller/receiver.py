from microbit import *
import radio
# Connect server to PC

### Notes ###

# All kitroniks with have my personal ID to send to, prob use time.sleep to avoid sending at the same time
# Randomised sleep can be used to help stop collisions

# Dictionary to store the latest data from each sensor


def receiveCommand(serverId: str):
    message = radio.receive()  # Check for incoming messages

    if message:
        display.show("R")
        sleep(200)
        try:
            eval(message)
        except:
            return 0
        display.clear()
        if not message.endswith("\n"):
            message += "\n"
        uart.write(message)
