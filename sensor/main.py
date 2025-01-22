from microbit import *
import radio
from metrics import read_metrics
from data import send_data

radio.config(channel=14, group=1,length=250)
radio.on()

sensor_id = "server141"
server_id = "server14C"

while True:
    incoming = radio.receive()
    if incoming:
        incomingDict = eval(incoming)
        if incomingDict["sender_id"] == sensor_id and incomingDict["server_id"] == server_id:
            if incomingDict["data"] == True:
                data = read_metrics(sensor_id)
                send_data(sensor_id, server_id, data)
        else:
            print("Data is incoming but is not for the device or is invalid")

    if button_a.is_pressed():
        data = read_metrics(sensor_id)
        send_data(sensor_id, server_id, data)



    incoming = radio.receive()
    if incoming:
        print(incoming)
