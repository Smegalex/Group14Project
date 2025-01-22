import radio


def send_data(sender_id, receiver_id, data):
    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))


def validate_data(sensor_id, server_id, incoming):
    print("Validatig data...")

    message = eval(incoming)

    if message["sender_id"] == server_id and message["receiver_id"] == sensor_id:
        print("Request validated!")
        return message
    else:
        print("Request invalid!")
        return False
