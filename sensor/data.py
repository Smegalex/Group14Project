import radio

radio.config(channel=14, group=1)
radio.on()


def send_data(sender_id, receiver_id, data):
    msg_dict = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(msg_dict)
