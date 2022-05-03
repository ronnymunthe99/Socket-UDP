from socket import *
host=gethostname();
serverPort=150
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('input lowercase sentence:')
clientSocket.sendto(message.encode(),(host,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(300)
print (modifiedMessage.decode())
clientSocket.close()
