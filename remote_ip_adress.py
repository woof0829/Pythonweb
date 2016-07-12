import socket
def get_remote_IPaddress():
	remote_host='www.pytgo.org'
	try:
		print"IP address of this website:%s"%socket.gethostbyname(remote_host)
	except socket.error,err_msg:
		print"%s:%s"%(remote_host,err_msg)

if __name__=='__main__':
	get_remote_IPaddress()