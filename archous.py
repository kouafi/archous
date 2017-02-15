#!/usr/local/bin/python3
import os, sys, getopt, time
import requests
import json
from urllib.request import urlopen
from urllib.parse import urlparse
from datetime import date

def main(argv):
	path = "storage/db.json"
	url = ""
	dl = None
	err_msg = "Usage: archous.py -u [url] -D.\nSee documentation: https://kvfi.github.io/archous/docs/0.1"
	err_msg_url = "Looks like \"{0}\" is not reachable.\nPlease verify your Internet connection."
	try:
		opts, args = getopt.getopt(argv,"hDu:i",["url=", 'init'])
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
			if url:
				dl = True
			else:
				print("Please specicy an URL.")
				print(err_msg)
	if os.path.exists(path) and os.path.getsize(path) > 0:
		if url:
			try:
				r = requests.head(url)
				# print(r.status_code)
				if (r.status_code == 404):
					continue404 = input("The URL you entered ({0}) has returned a 404 error. Do you want to save it anyways? [y/N]".format(url))
					if (continue404 == 'y'):
						print("ok lets save it")
					else:
						sys.exit(2)
				else:
					with open(path, "r+") as jsonFile:
					    data = json.load(jsonFile)
					    ids = []
					    for k in data:
					    	if k["Id"] != "":
					    		ids.append(k["Id"])
					    	if k["url"] == url:
					    		sys.exit(
					    			"The URL \"{0}\" has already been stored on {1}".format(
					    				url,
					    				time.strftime(
					    					"%a, %d %b %Y %H:%M:%S GMT",
					    					tuple(k["added"])
					    				)
					    			)
					    		)
					    if not ids:
					    	itemId = 0
					    else:
					    	itemId = max(ids) + 1

					    item = {"Id": itemId, "url": url, "added": time.gmtime()}

					    data.append(item)
					    jsonFile.seek(0)  # rewind
					    jsonFile.write(json.dumps(data))
					    jsonFile.truncate()
			except requests.ConnectionError:
				print(err_msg_url.format(url))
	else:
		print("WARNING: It looks like there is no storage file at the specified location.\nThe database file is supposed to be located at: {0}.\nIf you are running Archous for the first time, be sure to run:\npython archous.py --init".format(path))
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])