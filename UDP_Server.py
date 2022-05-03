from socket import *
serverPort=150
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while(True):
  message,clientAddress=serverSocket.recvfrom(300)
  modifiedMessage=message.decode().upper()
  serverSocket.sendto(modifiedMessage.encode(),clientAddress)
