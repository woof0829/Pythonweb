import socket

def convertinteger():
	data = 1234
	# 32-bit
	print "Original: %s => Long Host Byte Order: %s, Network Byte order: %s"%(data, socket.ntohl(data), socket.htonl(data))
	# 16-bit
	print "Original: %s => Short Host Byte Order: %s, Network Byte order: %s"%(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
	convertinteger()