from microbit import *
import radio

from metrics import read_metrics
from data import send_data

radio.config(channel=14, group=1)
radio.on()

sensor_id = "server140"
server_id = "server14C"

while True:
    if button_a.was_pressed():
        data = read_metrics(sensor_id)
        send_data(sensor_id, server_id, data)

    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
