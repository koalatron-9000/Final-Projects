from PIL import Image
import glob
import os
'''This script will batch process a folder of pictures and save them in a seperate folder.'''


GL = glob.glob("/insert/original/filepath/here/") #Glob searches a filepath and returns a list
NewD = "/instert/new/directory/here/" #Defines a target file path

for each in GL: #Iterates through the each item of the GL list
    s=os.path.split(each) #splits the the file name from the file path
    img = Image.open(each).rotate(270).resize((128, 128)) #Opens a file(each) and does operations
    img.save(NewD+s[1]) #Saves processed file in the new directory 

