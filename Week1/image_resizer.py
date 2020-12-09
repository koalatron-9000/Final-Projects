from PIL import Image
import glob

GL = glob.glob("/home/koalatron9000/Pictures/*.png")
for file in GL:
    print(file)