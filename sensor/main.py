from microbit import *
import radio
from data import *
from OLED import *

radio.config(channel=14, group=1, length=250)
radio.on()

sensor_id = "server142"
server_id = "server14S"

while True:
    show("Device ID: {}".format(sensor_id), 0)
    show("Ready To Recieve Data",7)
    recieve_data(sensor_id, server_id)
