#!/usr/local/bin/python3
import sys, getopt
from urllib.request import urlopen
from urllib.parse import urlparse

def main(argv):
	url = ''
	dl = None
	err_msg = 'Usage: archous.py -u [link] -D.\nSee documentation: https://kvfi.github.io/archous/docs/0.1'
	try:
		opts, args = getopt.getopt(argv,"hDu:",["url="])
	except getopt.GetoptError:
		print(err_msg)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(err_msg)
			sys.exit()
		elif opt in ("-u", "--url"):
			url = arg
		elif opt == '-D':
			dl = true
	
	a = urlopen('http://www.google.com/asdfsf')
	print(getcode())

if __name__ == "__main__":
	main(sys.argv[1:])