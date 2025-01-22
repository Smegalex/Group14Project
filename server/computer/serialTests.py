import serial
import time

portName = "COM9"  # add more variables for other portnames

personal_id = "server14S"
target_id = "fy23ot"

# Color codes for terminal text
GREEN = "\033[1;32m"
GRAY = "\033[0m"

# Initialize the serial connection to the MicroBit
connection = serial.Serial(port=portName, baudrate=115200, timeout=1)


def create_message(value):
    message = {'msg': value, 'sender_id': personal_id,
               'receiver_id': target_id}
    return message

def validate_message(message_dict):
    expected_keys = ['msg', 'sender_id', 'receiver_id']
    for key in expected_keys:
        if key not in message_dict:
            return False
    return True

def change_target(new_target):
    global target_id
    target_id = new_target

# List to store unseen messages
inbox = []


def send_message():
    global receiver_id 
    user_input = input(
        "Enter your message (type 'INBOX' to check messages): ")

    # If the user types 'INBOX', show all unseen messages
    if user_input.startswith("/"):
        if user_input.startswith("/target"):
            username = user_input.split("/target")
            username = username[1].strip()
            change_target(username)
            print(f"Messaging {receiver_id}")
    elif user_input.upper() == "INBOX":
        receive_messages()
        show_inbox()
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
        except:
            print("Invalid message received.")


def show_inbox():
    if inbox:
        print(f"{GREEN}--- INBOX ---{GRAY}")
        for msg in inbox:
            print(f"{GREEN}{msg['msg']}{GRAY}")
            print("\n")
        inbox.clear()  # Clear the inbox after showing messages
        print(f"{GREEN}--- END OF INBOX ---{GRAY}")
    else:
        print(f"{GREEN}Your inbox is empty.{GRAY}")


def main():
    while True:
        # Check for incoming messages and buffer them
        receive_messages()

        # Allow the user to send a message or check their inbox
        send_message()
        time.sleep(1)


# Run the main function
main()
