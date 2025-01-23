import radio
from OLED import *


def send_data(sender_id, receiver_id, data):
    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))


def validate_data(sensor_id, server_id, incoming,usedUUID):
    try:
        message = eval(incoming)
    except:
        return False

    if message["sender_id"] == server_id and message["receiver_id"] == sensor_id:
        print("Request validated!")
        return message
    elif message not in usedUUID:
        resend_message(incoming)
        
    else:
        return False
    
def resend_message(message):

    radio.send(str(message) + "\n")
    message["bounces"] +=1
    show(str(message) + " bounces with resend",3)
    print("Data resent!")
    print(str(message))

    
    