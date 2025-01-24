import serial
import time as timey
import random
import datetime
from csvFormatting import process_messages

portName = "COM9"  # add more variables for other portnames

personal_id = "server14S"
target_id = "sensor140"

# Color codes for terminal text
GREEN = "\033[1;32m"
GRAY = "\033[0m"

# Initialize the serial connection to the MicroBit
connection = serial.Serial(port=portName, baudrate=115200, timeout=1)
connection.set_buffer_size(rx_size=32000, tx_size=32000)


def create_message(value, receiver_id: str = None):
    message = {'data': value, 'sender_id': personal_id,
               'receiver_id': target_id, "uuid": random.randint(0, 100000), "bounces": 0}
    if receiver_id:
        message["receiver_id"] = receiver_id
    # print(message)
    return message


def validate_message(message_dict):
    expected_keys = ['data', 'sender_id', 'receiver_id']
    # print("message valid")
    for key in expected_keys:
        if key not in message_dict:
            return False
    return True


def change_target(new_target):
    global target_id
    target_id = new_target


listen = 0
run = True
used_uuids = []

defaultListen = 10


def loopey(time):
    time = listen_check(time)
    change_target("sensor140")
    message = str(create_message(time))+"\n"
    # print(message)
    connection.write(message.encode())
    timey.sleep(0.3)

    change_target("sensor141")
    message = str(create_message(time))+"\n"
    connection.write(message.encode())
    timey.sleep(0.3)

    change_target("sensor142")
    message = str(create_message(time))+"\n"
    connection.write(message.encode())
    timey.sleep(0.3)

    change_target("sensor143")
    message = str(create_message(time))+"\n"
    connection.write(message.encode())
    timey.sleep(0.3)

    update_listen(time+5)


def listen_check(time):
    try:
        time = int(time)
        listen = time
    except:
        listen = defaultListen
    return listen


def update_listen(time: int):
    global listen
    listen = listen_check(time)
    message = str(create_message(
        f"listen{listen}", "server14C")) + "\n"
    connection.write(message.encode())
    return listen


def send_message():
    global receiver_id
    user_input = input(
        f"Enter number of updates you want from {target_id}: ")

    if user_input.startswith("/"):
        global listen
        global run
        if user_input.startswith("/target") or user_input.startswith("/t"):
            username = ""
            if user_input.startswith("/target"):
                username = user_input.split("/target")
            else:
                username = user_input.split("/t")
            username = username[1].strip()
            change_target(username)
            print(f"Messaging {username}")
        elif user_input.startswith("/loop"):
            time = []
            time = user_input.split("/loop")
            time = time[1].strip()
            # print(time)
            loopey(time)
        elif user_input.startswith("/listen") or user_input.startswith("/l"):
            time = 0
            if user_input.startswith("/listen"):
                time = user_input.split("/listen")
            else:
                time = user_input.split("/l")
            time = time[1].strip()
            update_listen(time)
            print(f"Listening for {listen} seconds")
        elif user_input.startswith("/stop") or user_input.startswith("/s"):
            run = False
    else:
        message = str(create_message(user_input)) + "\n"
        connection.write(message.encode())


def receive_messages():
    while connection.in_waiting > 0:
        message = connection.readline().decode().strip()
        # Check if Message is valid dictionary format
        try:
            msg_dict = eval(message)
            # print(msg_dict)
            if validate_message(msg_dict):
                if msg_dict['receiver_id'] == personal_id:
                    if (isinstance(msg_dict["data"], dict)):
                        if not msg_dict['uuid'] in used_uuids:
                            msg_dict['data']['time'] = str(datetime.datetime.now())[:-7]
                            process_messages(msg_dict)
                            used_uuids.append(msg_dict['uuid'])
                            print(f"{GREEN}{msg_dict["sender_id"]}:{
                                GRAY} data dictionary received")
                    else:
                        print(f"{GREEN}{msg_dict["sender_id"]}:{
                              GRAY} {msg_dict['data']}")
        except:
            if not (message == "\n" or message == "" or message == " "):
                print("Invalid message received:")
                print(message)


def main():
    global listen
    while run:
        # Check for incoming messages and buffer them
        receive_messages()
        # Allow the user to send a message or check their inbox
        if listen <= 0:
            send_message()
            timey.sleep(0.3)

        if listen > 0:
            timey.sleep(0.05)
            listen += -0.05


# Run the main function
main()
