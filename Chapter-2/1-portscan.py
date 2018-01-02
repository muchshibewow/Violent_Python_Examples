#! /usr/bin/env python

# Written for the sole purpose of practice.
# Examples taken (and some modified) from Violent Python.

# Connects to a port on the target system, and tries to get
# a TCP ACK back, signifying an open port.

# This is also my first program with the optparse library.

from socket import *
import optparse

def connScan(host,ports):
	"""
	   Tries to connect on an open port on a host IP.
	   If unsuccessful, returns a "port closed" message.
	"""

	# Running through the list of ports
	for port in ports:

		# The socket object tries to connect to the port 
		# specified on the target IP, and throws an exception
		# when the connection fails.
		try:
			connection = socket.socket(AF_INET,SOCK_STREAM)
			connection.connect((host,port))

			# In order to grab some sort of banner, some random
			# data needs to be sent through the connection.
			connection.send("Lulz\r\n")
			banner = connection.recv(256)
			print '>> Port '+port+' on target IP '+host+' is open'
			if banner:
				print'>> Banner: \n'+banner
			else:
				print '>> No banner received.'
		except:
			print '>> The specified port is closed.'

# Typical boilerplate
def main():
	parser = optparse.OptionParser("python 1-portscan.py "+"-H <host IP> "+"-p <target port(s), comma separated>")
	parser.add_option('-H',dest="host",type="string",help="The target IP address")
	parser.add_option('-p',dest="ports",type="string",help="The list of target ports on the IP")
	(options,args) = parser.parse_args()
	host = options.host
	ports = list(map(int,str(options.ports).split(",")))
	connScan(host,ports)

if __name__ == '__main__':
	main()