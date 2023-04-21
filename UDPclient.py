import socket

msgFromClient = input("enter input here: ")
bytesToSend = str.encode(msgFromClient.lower())
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 65432
ADDR = (SERVER, PORT)
serverAddressPort = (ADDR)
bufferSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format (msgFromServer[0])
print(msg)