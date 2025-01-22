from microbit import *
import radio

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
