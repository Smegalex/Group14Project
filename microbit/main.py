from microbit import *
import radio

radio.config(channel=14, group=1)
radio.on()


while True:
    if button_a.was_pressed():
        display.scroll(8)
        radio.send("Colonel Al reporting for duty!")

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)

