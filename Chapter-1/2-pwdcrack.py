#! /usr/bin/env python

# Written for the sole purpose of practice.
# Examples taken (and some modified) from Violent Python.

# This is the original example present in the book,
# based on the UNIX crypt() function.

from crypt import crypt
import sys

def testPass(passFile,dictFile):
	"""
		Checks if the hash in the passFile corresponds to 
	    any of the words in the dictFile, using the salt 
	    from the first 2 bytes of the hsah itself.
	"""

	# The password file contains just the single hashed password.
	# The salt is the first 2 characters of the hash.
	passwd = open(passFile,"r").readlines()[0]
	salt = passwd[0:2]

	# The dictionary file contains potential password candidates.
	dictionary = open(dictFile,"r")

	found = False
	for word in dictionary.readlines():
		
		# The hash is "calculated" using the crypt() function,
		# present in the crypt library. It takes the word and 
		# the salt as arguments.
		word = word.strip("\n")
		if crypt(word,salt) == passwd:
			print ">> Password found : "+word
			found = True
			break
	if not found:
		# Password is not present in dictionary.
		print ">> Password not found in the dictionary provided."

def main():
	if len(sys.argv) == 3:
		testPass(sys.argv[1],sys.argv[2])
	else:
		print "Usage : python 2-pwdcrack.py <passwordfile> <dictionaryfile>"
		print "For sample usage, use cryptpass.txt and dictionary.txt from this folder."
		exit(0)

if __name__ == '__main__':
	main()