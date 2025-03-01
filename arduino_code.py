# import serial.tools.list_ports
#
# ports = serial.tools.list_ports.comports()
# for port in ports:
#     print(port.device)
#
# import serial
# import time
#
# arduino = serial.Serial(port='COM3', baudrate=115200, timeout=2)
# time.sleep(3)  # Allow Arduino to initialize
#
# if arduino:
#     print("[INFO] Sending unlock signal to Arduino...")
#     arduino.write(b'o')  # Equivalent to bytes('o', 'utf-8')
#     time.sleep(5)
#
#     print("DOOR is about to be closed")
#     arduino.write(b'c')



import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))


com = input("Select COM port for arduino #:")

for i in range(len(portsList)):
    if portsList[i].startswith("COM"+str(com)):
        use = "COM" + str(com)

        print(use)


serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()


while True:
    command = input("Arduino Command (o/c):")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        exit()


