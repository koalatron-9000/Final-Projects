from PIL import Image
import glob
import os

GL = glob.glob("/home/koalatron9000/Pictures/*.png")
NewD = "/reworked/"
for each in GL:
    print(each)
    s=os.path.split(each)
    img = Image.open(each).rotate(270).resize((128, 128))
    img.save(s[0]+NewD+s[1])

