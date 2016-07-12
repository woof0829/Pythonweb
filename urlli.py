import urllib

handler=urllib.urlopen("http://www.py4inf.com/code/romeo.txt")
for line in handler:
	print line.strip()