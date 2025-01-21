from microbit import *
import radio

radio.config(channel=14, group=1)
radio.on()
uart.init(baudrate=115200)

while True:
    if button_a.was_pressed():
        display.show(8)
        radio.send("Alex")

    if button_b.was_pressed():
        uart.write("Hello World!\n")

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)

    pcMessage = uart.read()
    if pcMessage:
        pcMessage = "microbit: {}\n".format(str(pcMessage.decode()))
        uart.write(pcMessage)
