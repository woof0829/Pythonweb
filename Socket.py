import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.py4inf.com', 80))
sock.send('GET http://www.py4inf.com/code/remeo.txt HTTP/1.0\n\n')#Telnet命令 包含了Http1.0协议

while True:
    data = sock.recv(512)#recevie
    if ( len(data) < 1 ) :
        break
    print data
sock.close()
#http Request