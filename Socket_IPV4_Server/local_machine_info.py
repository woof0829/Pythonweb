import socket

def machineinfo():
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	print "Host name:", host_name
	print "IP address:", ip_address

if __name__ == '__main__':
	machineinfo()