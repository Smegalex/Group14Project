from microbit import *
import radio

from sender import sendCommand
from receiver import receiveCommand

display.clear()

radio.config(channel=14, group=1, length=250)
radio.on()

controllerId = "server14C"
serverId = "server14S"

listenDuration = 0


def changeListen(newAmount: int):
    global listenDuration
    listenDuration = newAmount


while True:
    receiveCommand(serverId)

    if listenDuration > 0:
        display.show("L")
        sleep(50)
        listenDuration += -0.05
    else:
        sleep(200)
        sendCommand(controllerId, serverId, changeListen)
