from microbit import *
import radio


def sendCommand(controllerId: str, serverId: str):
    pcMessage = uart.read()

    if pcMessage:
        pcMessage = pcMessage.decode()
        try:
            eval(pcMessage)
        except:
            return 0
        pcMessage = str(pcMessage) + "\n"
        radio.send(pcMessage)
        commandConfirmation = {"msg": "Command sent succesfully.",
                               "sender_id": controllerId, "receiver_id": serverId}
        uart.write(str(commandConfirmation)+"\n")
