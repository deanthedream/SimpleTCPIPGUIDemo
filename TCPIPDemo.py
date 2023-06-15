#TCPIPDemo


import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = s.getsockname()
s.bind(('', TCP_PORT)) #Bind to the port
s.connect((TCP_IP, TCP_PORT))
try:
    s.send(MESSAGE.encode('utf-8'))
except:
    s.close()
try:
    data = s.recv(BUFFER_SIZE)
except:
    s.close()
s.close()
  
print("received data:", data)

