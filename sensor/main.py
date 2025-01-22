from microbit import *
import radio
from data import *

radio.config(channel=14, group=1, length=250)
radio.on()

sensor_id = "server140"
server_id = "server14S"

while True:
    recieve_data(sensor_id, server_id)
