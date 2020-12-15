import os
import json
import requests

files = "/home/koalatron9000/Documents/github/course 6 finals/Final-Projects/Week2"
reviews = os.listdir(files)
#r = requests.post("https://httpbin.org/post")
#print(r)

for each in reviews:
    with open(each, "r") as f:
        ReadData = list(f)
        payload = {"title":str(ReadData[0]).replace("\n",""),
        "name":str(ReadData[1]).replace("\n",""),
        "date":str(ReadData[2]).replace("\n",""),
        "feedback":str(ReadData[3:]).replace("\n","")}
        r = requests.post("https://httpbin.org/post", data=payload)
        print(r)