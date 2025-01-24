from microbit import *
import radio
from OLED import *
from data import *
from metrics import *
from audio import * 


global usedUUID
usedUUID = []
radio.config(channel=14, group=1, length=250)
radio.on()

init_display()
device_id_not_selected = True
sensor_id = 140
play(Sound.HAPPY)


while device_id_not_selected:
    show("Press A to add 1",1)
    show("Press B to finish",2)
    show("Sensor ID:"+str(sensor_id),4)
    if button_a.is_pressed():
        sensor_id += 1
        if sensor_id == 150:
            sensor_id = 140
    if button_b.is_pressed():
        sensor_id = "sensor"+str(sensor_id)
        device_id_not_selected = False
        show("",1)
        show("",4)

server_id = "server14S"

while True:
    if len(usedUUID) > 30:
        usedUUID = []

    show("Device ID: {}".format(sensor_id), 0)
    show("Server ID: {}".format(server_id), 7)
    show("Ready to send/receive", 2)

    incoming = radio.receive()

    if incoming:
        show("Incoming data.", 3)
        print("Request received!")
        print("Validating request...")

        validated,usedUUID = validate_data(sensor_id, server_id, incoming,usedUUID)

        if validated:
            count = 1

            try:
                count = int(validated["data"])
            except:
                print("Error reading count!")


            show("Sending data.", 3)

            for i in range(count):
                print("Reading metrics...")
                data = read_metrics(sensor_id)

                print("Sending data count: {}...".format(i + 1))
                usedUUID = send_data(sensor_id, server_id, data,usedUUID)

                sleep(1000)
            show("Data sent!", 3)
        else:
            print("Request not for us!")
