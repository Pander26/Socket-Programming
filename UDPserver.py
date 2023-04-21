import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 65432
ADDR = (SERVER, PORT)
bufferSize = 1024

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind(ADDR)

print("UDP server up and listening")

while(True) :

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)

    print(clientMsg)
    print(clientIP)

    msgFromServer = clientMsg.upper()
    bytesToSend = str.encode(msgFromServer)

    UDPServerSocket.sendto(bytesToSend, address)
