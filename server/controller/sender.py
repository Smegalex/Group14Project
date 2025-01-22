from microbit import *
import radio


def sendCommand(controllerId, serverId, changeListen):
    display.show("S")

    pcMessage = uart.read()

    if pcMessage:
        pcMessage = pcMessage.decode()
        pcMessage_dict = {}

        try:
            pcMessage_dict = eval(pcMessage)
        except:
            return 0

        if not pcMessage_dict["receiver_id"] == controllerId:
            # display.show("M")
            # sleep(100)
            pcMessage = str(pcMessage) + "\n"
            radio.send(pcMessage)

            confirm = {
                "data": "Command sent succesfully",
                "sender_id": controllerId,
                "receiver_id": serverId
            }

            uart.write((str(confirm)+"\n"))
        else:
            display.show("C")
            sleep(100)
            command = pcMessage_dict["data"]
            if command.startswith("listen"):
                duration = command.split("listen")[0]
                try:
                    duration = int(duration)
                    changeListen(duration)
                except:
                    changeListen(10)
