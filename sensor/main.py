from microbit import *
import radio

from OLED import *

from data import *
from metrics import *

radio.config(channel=14, group=1, length=250)
radio.on()

init_display()

sensor_id = "sensor140"
server_id = "server14S"

while True:
    show("Device ID: {}".format(sensor_id), 0)
    show("Ready!", 4)

    incoming = radio.receive()

    if incoming:
        print("Request received!")
        print("Validating request...")

        validated = validate_data(sensor_id, server_id, incoming)

        if validated:
            count = 1

            try:
                count = int(validated["data"])
            except:
                print("Error reading count!")

            show("Sending data...", 4)

            for i in range(count):
                print("Reading metrics...")
                data = read_metrics(sensor_id)

                print("Sending data count: {}...".format(i + 1))
                send_data(sensor_id, server_id, data)

                sleep(1000)

            show("Data sent", 4)
        else:
            print("Request not for us!")
