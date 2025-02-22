import radio
import random
from OLED import *


def send_data(sender_id, receiver_id, data, usedUUID):
    message = {"sender_id": sender_id, "receiver_id": receiver_id,
               "data": data, "uuid": random.randint(1, 100000), "bounces": 0}
    usedUUID.append(message["uuid"])
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))
    return usedUUID


def validate_data(sensor_id, server_id, incoming, usedUUID: list, commandUUID: list, broadband_id: str = "sensor140"):
    try:
        message = eval(incoming)
    except:
        return False, usedUUID
    print("incoming UUID =", message["uuid"])
    show("UUID=" + str(message["uuid"]), 5)
    if message["sender_id"] == server_id and message["receiver_id"] == broadband_id and message["uuid"] not in commandUUID:
        print("Broadband request validated!")
        commandUUID.append(message["uuid"])
        resend_message(incoming, usedUUID)
        return message, usedUUID, commandUUID
    elif message["sender_id"] == server_id and message["receiver_id"] == sensor_id and message["uuid"] not in commandUUID:
        print("Request validated!")
        commandUUID.append(message["uuid"])
        return message, usedUUID, commandUUID
    elif message['sender_id'] == sensor_id:
        return False, usedUUID, commandUUID
    elif message["uuid"] not in usedUUID:
        usedUUID.append(message["uuid"])
        resend_message(incoming, usedUUID)
        return False, usedUUID, commandUUID
    else:
        usedUUID.append(message["uuid"])
        return False, usedUUID, commandUUID


def resend_message(message, usedUUID):
    radio.send(str(message))
    # show("data to" + message["receiver_id"],3)
    print(usedUUID)
