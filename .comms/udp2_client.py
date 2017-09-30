# Echo server program
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50011              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
try:
    while 1:
        data = conn.recv(1024)
        if (data):
            print data
            conn.sendall(data)
        #if not data: break
except Exception as e:
    print e
    conn.close()
