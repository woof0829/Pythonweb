import socket
from binascii import hexlify #use hex stand for binary

def convert_ipv4address():
	for ipaddr in ['127.0.0.1', '192.168.0.1']:
		packed_ipaddr = socket.inet_aton(ipaddr)
		unpacked_ipaddr = socket.inet_ntoa(packed_ipaddr)
		print "IP address: %s => Packed: %s, Unpacked: %s"%(ipaddr, hexlify(packed_ipaddr), unpacked_ipaddr)

if __name__ == '__main__':
	convert_ipv4address()