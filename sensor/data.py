import radio
from metrics import read_metrics

def send_data(sender_id, receiver_id, data):
    print("Sending data...")

    message = {"sender_id": sender_id, "receiver_id": receiver_id, "data": data}
    radio.send(str(message) + "\n")

    print("Data sent!")
    print(str(message))

def recieve_data(sensor_id,server_id):
    incoming = radio.receive()
    if incoming:
        incomingDict = eval(incoming)
        if incomingDict["sender_id"] == sensor_id and incomingDict["receiver_id"] == server_id:
                data = read_metrics(sensor_id)
                send_data(sensor_id, server_id, data)
        else:
            print("Data is incoming but is not for the device or is invalid")