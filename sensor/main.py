from microbit import *
import radio

from OLED import *

from data import *
from metrics import *

radio.config(channel=14, group=1, length=250)
radio.on()

sensor_id = "sensor140"
server_id = "server14S"

while True:
    show("Device ID: {}".format(sensor_id), 0)
    show("Ready To Recieve Data", 7)

    incoming = radio.receive()

    if incoming:
        print("Data received!")
        print("Decoding data...")

        validated = validate_data(sensor_id, server_id, incoming)

        if validated:
            count = int(validated["data"])

            print("Reading metrics...")
            data = read_metrics(sensor_id)

            print("Sending data {} times...".format(count))
            for i in range(count):
                send_data(sensor_id, server_id, data)
                sleep(1000)
        else:
            print("Not sending data!")
