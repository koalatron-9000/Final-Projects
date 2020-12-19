import requests
import glob

#upload images from "/supplier-data/images/" to the website.
#	use example_upload.py as a base for this file.
#	url will be [linux-instance-IP-Address]/upload
#	import requests X
url = "[linux-instance-IP-Address]/upload/"
GL = glob.glob("/home/koalatron9000/Pictures/*.jpeg")
for each in GL:
    with open(each,"rb") as opened:
        requests.post(url, files ={"file": opened})
         