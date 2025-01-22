from microbit import *
import radio
from send import sendCommand

radio.config(channel=14, group=1)
radio.on()
controllerId = "server14C"
serverId = "server14S"

while True:
    sleep(1000)
    sendCommand(controllerId, serverId)
