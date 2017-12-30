#! /usr/bin/env python

# Written for the sole purpose of practice.
# Examples taken (and some modified) from Violent Python.

# Didn't exactly work, though. The IPs I tried this with were down.

import socket,os,sys

def retBanner(ip,port):
	"""
		Returns the banner sent by the port on the target ip.
	"""
	try:
		socket.setdefaulttimeout(5) #Bad internet connection ('._.)
		s = socket.socket() #New socket object
		print '>> Connecting to port '+str(port)+' on IP address '+ip

		# The following line connects the socket object created above
		# to the IP address and port passed to this function.
		# For the connect() function used here, the IP socket 
		# requires a 2-tuple in the form of (IP, port).
		s.connect((ip,port))
		print '>> Connected.'

		# Now, the socket receives the banner from the server,
		# and returns it. The buffer length is set to be 1KB,
		# or 1024 bytes (I guess).
		print '>> Receiving.'
		banner = s.recv(1024)

		return banner
	except:
		# Connecting the socket did not succeed for some weird reason.
		print 'The host might be down, connection did not succeed.'
		return None

def checkVulns(banner,vulnFile):
	"""	
	    Checks the banner against a list of vulnerable banners
		passed as an argument to the program.
	"""
	vulns = open(vulnFile,'r') #Opening the vulnerable server file in read mode.
	flagVar = True #Boolean for checking if the server is vulnerable or not. 
	for vulnBanner in vulns.readlines():
		if vulnBanner.strip('\n') in banner:
			print ">> The server is vulnerable.\n Banner : "+vulnBanner
			flag = False
			break
	if flagVar:
		print ">> The server is not vulnerable."

def main():
	# Edit this IP list to the ones you want to use.
	ip_list = ['47.11.231.'+str(i) for i in range(189,200)] #47.11.231.189 to 47.11.231.199
	port = 21 #Port 21 is the FTP port.
	# Checking the file passed as an argument to the program.
	if len(sys.argv) == 2:

		# The first argument is the program itself,
		# followed by the rest of the arguments.
		filename = sys.argv[1]

		# If the file doesn't exist : 
		if not os.path.isfile(filename):
			print "The file specified doesn't exist."
			exit(0)

		# If the current user doesn't have read permission for the file : 
		if not os.access(filename,os.R_OK): #R_OK is a flag that means "Read OK"
			print "Access to "+filename+" denied"
			exit(0)

	else:
		# The user did not specify the filepath.
		print "Usage : python 1-vulncheck.py <filename> OR ./1-vulncheck.py <filename>"
		exit(0)

	# Looping through the IPs in the list, and scanning individually.
	for ip in ip_list:

		# Calling the retBanner() function.
		banner = retBanner(ip,port)

		# Checking the banner for vulnerabilities.
		if banner:
			print ">> Banner received. Checking for vulnerabilities.."
			checkVulns(banner,filename)

# Typical boilerplate
if __name__ == '__main__':
	main()
