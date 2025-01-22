import radio
from metrics import read_metrics


def send_data(sender_id, receiver_id, data):
    print("Sending data...")

    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))


def recieve_data(sensor_id, server_id):
    incoming = radio.receive()

    if incoming:
        print("Data received!")
        print("Decoding data...")

        message = eval(incoming)

        print("Validating data...")

        if message["sender_id"] == sensor_id and message["receiver_id"] == server_id:
            print("Request validated, sending data back!")

            data = read_metrics(sensor_id)
            send_data(sensor_id, server_id, data)
        else:
            print("Data received from unknown source.")
