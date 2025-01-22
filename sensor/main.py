from microbit import *
import radio

from OLED import *

from data import *
from metrics import *

radio.config(channel=14, group=1, length=250)
radio.on()

sensor_id = "server140"
server_id = "server14S"

while True:
    show("Device ID: {}".format(sensor_id), 0)
    show("Ready To Recieve Data", 7)

    incoming = radio.receive()

    if incoming:
        print("Data received!")
        print("Decoding data...")

        valid = validate_data(sensor_id, server_id, incoming)

        if valid:
            print("Reading metrics...")
            data = read_metrics(sensor_id)

            print("Sending data...")
            send_data(sensor_id, server_id, data)
        else:
            print("Not sending data!")
