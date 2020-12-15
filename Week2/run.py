import os
import requests

files = "/path/to/files"
reviews = os.listdir(files)

for each in reviews:
    with open(each, "r") as f:
        ReadData = list(f)
        payload = {"title":str(ReadData[0]).replace("\n",""),
        "name":str(ReadData[1]).replace("\n",""),
        "date":str(ReadData[2]).replace("\n",""),
        "feedback":str(ReadData[3:]).replace("\n","")}
        r = requests.post("website.address/endpoint", data=payload)
        print(r)