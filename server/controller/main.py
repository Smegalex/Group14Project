from microbit import *
import radio
from sender import sendCommand
from receiver import receiveCommand

display.clear()
radio.config(channel=14, group=1, length=250)
radio.on()
controllerId = "server14C"
serverId = "server14S"

while True:
    receiveCommand(serverId)
    sleep(200)
    sendCommand(controllerId, serverId)
