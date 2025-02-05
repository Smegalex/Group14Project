import radio
from microbit import *
from audio import *
play(Sound.TWINKLE)


radio.config(channel=14, group=1, length=250)
radio.on()
usedUUID = []
while True:
    if len(usedUUID) > 30:
        usedUUID = []
    incoming = radio.receive()
    display.show("r")
    if incoming:
        display.show("i")
        try:
            message = eval(incoming)
        except:
            pass
        if message["uuid"] not in usedUUID:
            usedUUID.append(message["uuid"])
            radio.send(str(message))
            print(usedUUID)
            print("Data resent!")
