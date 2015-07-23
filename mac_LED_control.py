import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.22'
port = 7174 

s.connect((host,port))
print "Connected to ", host
initialMessage = s.recv(1024)
print initialMessage
#s.sendall("Hello Pi")
try:
	while True:
		answer=raw_input(">: ")
		s.sendall(answer)

except KeyboardInterrupt:
	s.close()

