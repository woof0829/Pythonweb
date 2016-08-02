import socket

def find_servicename():
	protocal_name = 'TCP'
	for port in [80,25]:
		print "Port:%s => service name: %s"%(port, socket.getservbyport(port, protocal_name))
	print "Port:%s => service name: %s"%(53, socket.getservbyport(53, 'UDP'))

if __name__ == '__main__':
	find_servicename()