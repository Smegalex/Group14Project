from microbit import *
from OLED import *
from getData import *
import radio
init_display()

DEVICEID = 1 #change for each device
data = getData(DEVICEID) #gets data as a dictionary


radio.config(channel=14, group=1)
radio.on()
uart.init(baudrate=115200)

while True:
    if button_a.was_pressed():
        display.show(8)
        radio.send("Alex")

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)

