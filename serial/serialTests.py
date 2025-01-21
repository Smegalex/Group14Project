import serial

portName = "COM9"

port = serial.Serial(port=portName, baudrate=115200, timeout=1)
if not port.isOpen():
    port.open()
print("Started")

while True:
    userMessage = input("PC: ")

    port.write(userMessage.encode())

    microbitMessage = port.readline().decode().strip()
    if microbitMessage:
        print(microbitMessage)
