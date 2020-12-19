import os
import requests

#process each text file into the format below and push it to the website.
#	remove "lbs" from the weight and turn into an integer
#	format will be: {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}
#	url will be http://[linux-instance-external-IP]/fruits
#	import os X
#	import requests X
files = "/home/koalatron9000/test"
reviews = os.listdir(files)

for each in reviews:
    with open(each, "r") as f:
        ReadData = list(f)
        payload = {"name":str(ReadData[0]).replace("\n",""),
        "weight":str(ReadData[1][:-4]).replace("\n",""),
        "description":str(ReadData[2:]).replace("\n","")}
        r = requests.post("http://[linux-instance-external-IP]/fruits", data=payload)
        print(r)
        