import os
import requests

#process each text file into the format below and push it to the website.
#	remove "lbs" from the weight and turn into an integer
#	format will be: {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}
#	url will be http://[linux-instance-external-IP]/fruits
#	import os X
#	import requests X