import radio


def send_data(sender_id, receiver_id, data):
    print("Sending data...")

    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))
