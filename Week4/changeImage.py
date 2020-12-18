from PIL import Image
import glob

'''This script will batch process a folder of pictures and save them in a seperate folder.'''

GL = glob.glob("/home/koalatron9000/Pictures/*.png") #Glob searches a filepath and returns a list

for each in GL: #Iterates through the each item of the GL list
    img = Image.open(each).resize((600, 400)) #Opens a file(each) and does operations
    img = img.convert("RGB") #Converts the RGBA files to RGB
    name = each.split(".") #Splits the file name from the file extention
    file_extension = ".jpeg" #New file extension
    new_name = str(name[0]) +file_extension #Combines the file name with the new extension
    img.save(new_name, "JPEG") #Saves processed file 
    
