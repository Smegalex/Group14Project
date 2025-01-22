import serial
import time

portName = "COM9"  # add more variables for other portnames

personal_id = "server14S"
target_id = "sensor140"

# Color codes for terminal text
GREEN = "\033[1;32m"
GRAY = "\033[0m"

# Initialize the serial connection to the MicroBit
connection = serial.Serial(port=portName, baudrate=115200, timeout=1)


def create_message(value):
    message = {'data': value, 'sender_id': personal_id,
               'receiver_id': target_id}
    return message


def validate_message(message_dict):
    expected_keys = ['data', 'sender_id', 'receiver_id']
    print("message valid")
    for key in expected_keys:
        if key not in message_dict:
            return False
    return True


def change_target(new_target):
    global target_id
    target_id = new_target


inbox = []
listen = 0


def send_message():
    global receiver_id
    user_input = input(
        "Enter your message: ")

    if user_input.startswith("/"):
        global listen
        if user_input.startswith("/target"):
            username = user_input.split("/target")
            username = username[1].strip()
            change_target(username)
            print(f"Messaging {username}")
        if user_input.startswith("/listen"):
            time = user_input.split("/listen")
            time = time[1].strip()
            try:
                time = int(time)
                listen = time
            except:
                listen = 10

            print(f"Listening for {listen} seconds")
    else:
        message = str(create_message(user_input)) + "\n"
        connection.write(message.encode())


def receive_messages():
    while connection.in_waiting > 0:
        message = connection.readline().decode().strip()
        # Check if Message is valid dictionary format
        try:
            msg_dict = eval(message)
            if validate_message(msg_dict):
                if msg_dict['receiver_id'] == personal_id:
                    inbox.append(msg_dict)
                    if (isinstance(msg_dict["data"], dict)):
                        print(f"{GREEN}{msg_dict["sender_id"]}:{GRAY} data dictionary received")
                    else:
                        print(f"{GREEN}{msg_dict["sender_id"]}:{GRAY} {msg_dict['data']}")
        except:
            print("Invalid message received.")


def main():
    global listen
    while True:
        # Check for incoming messages and buffer them
        receive_messages()

        # Allow the user to send a message or check their inbox
        if listen <= 0:
            send_message()
        time.sleep(0.2)
        if listen > 0:
            listen += -0.2


# Run the main function
main()
