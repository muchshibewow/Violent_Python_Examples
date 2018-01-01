#! /usr/bin/env python

# Written for the sole purpose of practice.
# Examples taken (and some modified) from Violent Python.

# Sample zip included in the repo.

import zipfile,sys

def testzip(zipFile,dictFile):
	"""
	    Uses list of passwords from the dictFile
	    to extract files from zipFile.
	"""

	# Opening the zip file in read mode.
	zip = zipfile.ZipFile(zipFile, mode = "r")
	dictionary = open(dictFile,'r').readlines()
	found = False
	for word in dictionary:
		word = word.strip("\n")
		print '>> Testing password : ' + word
		try:

			# zip.extractall() throws an exception
			# if the password for the file is 
			# incorrect, hence the try - except block.
			zip.extractall(pwd = word)
			print '>> Password found : ' + word
			found = True
			break
		except:

			# If not found, continue looking through the dictionary.
			continue
	if not found:
		print 'Password not present in dictionary!'

# Typical boilerplate
def main():
	if len(sys.argv) == 3:
		testzip(sys.argv[1],sys.argv[2])
	else:
		print 'Usage : python 4-zipcrack.py <zipfile> <dictionaryfile>'
		print 'For sample usage, use sample.zip and dictionary.txt'
		exit(0)

if __name__ == '__main__':
	main()
