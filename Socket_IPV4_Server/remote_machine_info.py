import socket

def remote_hostname():
	remote_host = 'www.google.com'
	try:
		print "IP address of remote host:", socket.gethostbyname(remote_host)
	except socket.error, err_msg:
		print "%s:%s"%(remote_host, err_msg)
	# if not a website match, return the execpt message
if __name__ == '__main__':
	remote_hostname()