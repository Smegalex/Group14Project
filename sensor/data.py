import radio
import random
from OLED import *


def send_data(sender_id, receiver_id, data,usedUUID):
    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data,"uuid":random.randint(1,100000),"bounces":0}
    usedUUID.append(message["uuid"])
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))
    return usedUUID


def validate_data(sensor_id, server_id, incoming,usedUUID):
    try:
        message = eval(incoming)
    except:
        return False,usedUUID
    print("incoming UUID =",message["uuid"])
    if message["sender_id"] == server_id and message["receiver_id"] == sensor_id and message["uuid"] not in usedUUID:
        print("Request validated!")
        usedUUID.append(message["uuid"])
        return message,usedUUID
    elif message['sender_id']==sensor_id:
        return False, usedUUID
    elif message["uuid"] not in usedUUID:
        usedUUID.append(message["uuid"])
        resend_message(incoming,usedUUID)
        return False,usedUUID
    else:
        usedUUID.append(message["uuid"])
        return False,usedUUID
    
def resend_message(message,usedUUID):
    radio.send(str(message))
    show("resent message",2)
    print(usedUUID)
    print("Data resent!")

    
    