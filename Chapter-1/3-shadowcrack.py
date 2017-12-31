#! /usr/bin/env python

# Written for the sole purpose of practice.
# Examples taken (and some modified) from Violent Python.

# Didn't actually learn how the shadow file precisely functions;
# However, most Linux based OSs use SHA-512 ($6$) nowadays, which
# is present in the crypt() library function.

import sys
from crypt import crypt

def testPass(passFile,dictFile):
	""" 
	    Tests the hashes of a list of words present in 
	    the dictFile agains the hash of the password 
	    present in the passFile, replicating the password
	    field for a user in the file /etc/shadow.
	"""

	# The passFile contains various ':' separated fields,
	# of which the 1st is the username, and the 2nd is
	# the hash of the password itself.
	pwd = open(passFile,'r').readlines()[0].strip().split(":")
	user,hash = pwd[0],pwd[1]

	# The salt is the combination of the encryption method
	# (SHA-512 represented as $6$) and the randomly generated
	# data.
	salt = '$6$' + hash.split('$')[2]

	# Looping through the dictionary for words.
	dictionary = open(dictFile,"r")
	found = False
	for word in dictionary.readlines():
		word = word.strip("\n")
		if crypt(word,salt) == hash:
			print '>> Password for user '+user+' found : '+word
			found = True
			break
	if not found:
		print '>> Password for user '+user+' not present in dictionary!'


# Typical boilerplate.
def main():
	if len(sys.argv) == 3:
		testPass(sys.argv[1],sys.argv[2])
	else:
		print 'Usage : python 3-shadowcrack.py <passwordfile> <dictionaryfile>'
		print 'For sample usage, use password.txt and dictionary.txt.'
		exit(0)

if __name__ == '__main__':
	main()
