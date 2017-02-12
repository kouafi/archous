#!/usr/bin/env python
import json
import os

a_dict = {'new_key': 'new_value'}

file = 'storage/links.json'
if os.path.exists(file) and os.path.getsize(file) > 0:
	with open(file) as f:
		data = json.load(f)

	data.update(a_dict)

	with open(file, 'w') as f:
	    json.dump(data, f)
else:
	print("ERROR: The file \"" + file + "\" does not exist or is empty.\nPlease double-check. If you want to initialize a new file, please run:\npython archous.py init")