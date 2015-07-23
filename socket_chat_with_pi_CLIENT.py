#basic server side of the two way communication
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.12'
port = 6969

s.connect((host,port))
print "Connected to ", host
initialMessage = s.recv(1024)
print initialMessage
s.sendall("Hello Pi")
while True:
	data = s.recv(1024)
	print "Message from Pi: ", data
	response = raw_input("Reply: ")
	
	s.sendall(response)
	if response == "exit":
		break	
	
s.close()

