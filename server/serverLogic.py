from visual.visualisation import display, DATATYPE_CONVERSION, print_allowed_datatypes, VALID_SENSORS
import serial
import time as timey
import random
import datetime
from dataProcessing.csvFormatting import process_messages
import threading
import multiprocessing


portName = "COM9"  # add more variables for other portnames

personal_id = "server14S"
target_id = "sensor140"


# Color codes for terminal text
GREEN = "\033[1;32m"
RED = "\033[1;31m"
GRAY = "\033[0m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"


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
    try:
        target_id = "sensor"+str(int(new_target))
    except ValueError:
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


def update_listen(time: int) -> int:
    global listen
    listen = listen_check(time)
    message = str(create_message(
        f"listen{listen}", "server14C")) + "\n"
    connection.write(message.encode())
    return listen


def command_display(user_input: str) -> None:
    """
    First argument - sensor numbers (multiple allowed); default - current target sensor; use 140 for all non empty sensors to be displayed
    Second argument - type of data we are interested in (temp, humidity etc.); default - display 4 graphs simultaneously. 
    """
    args = ''
    if user_input.startswith("/display"):
        args = user_input.split("/display")
    else:
        args = user_input.split("/d")
    args = args[1].strip()
    args = args.split(" ")
    args = [x.strip() for x in args if not x == None]
    sensors = None
    try:
        sensors = target_id.lower().replace("sensor", "")
        sensors = int(sensors)
    except ValueError:
        pass

    datatype = None

    if len(args) == 1:
        try:
            sensors = int(args[0].strip())
        except ValueError:
            datatype = args[0].strip()
    elif len(args) > 1:
        for arg in args:
            try:
                sensor = int(arg)
                if isinstance(sensors, int):
                    sensors = []
                sensors.append(sensor)
            except ValueError:
                try:
                    datatype = DATATYPE_CONVERSION[arg]
                except KeyError:
                    pass
    if datatype == None or not datatype or datatype == " ":
        datatype = "display 4"
        print(
            f"{YELLOW}No datatype detected. Default of displaying 4 graphs is applied.{GRAY}\n{GREEN}List of allowed datatypes for future reference:{GRAY}")
        print_allowed_datatypes()

    if sensors == None or not sensors or sensors == " ":
        print(f"{RED}No sensor ids have been selected and there is no valid target sensor.\n{
              WHITE}Fallback to calling 140 (all non empty sensors will be displayed).{GRAY}")
        sensors = 140

    # thread = threading.Thread(
    #     target=display, args=(sensors, datatype), daemon=True)
    process = multiprocessing.Process(
        target=display, args=(sensors, datatype), daemon=True)
    process.start()


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
            print(f"Messaging {target_id}")
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
        elif user_input.startswith("/display") or user_input.startswith("/d"):
            command_display(user_input)
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
                            msg_dict['data']['time'] = str(
                                datetime.datetime.now())[:-7]
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


if __name__ == "__main__":
    # Initialize the serial connection to the MicroBit
    global connection
    connection = serial.Serial(port=portName, baudrate=115200, timeout=1)
    connection.set_buffer_size(rx_size=32000, tx_size=32000)
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
