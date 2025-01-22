from microbit import *
import radio
from data import *

radio.config(channel=14, group=1, length=250)
radio.on()

sensor_id = "server141"
server_id = "server14C"

while True:
    recieve_data(sensor_id,server_id)
    
    incoming = radio.receive()
    if incoming:
        print("Data received!")
        print(incoming)
