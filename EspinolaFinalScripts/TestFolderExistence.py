#Question 3- First write a small code to create two new folders(see folder names below) inside your "LastnameFinal" folder,
#can you test if the folders already exist, if they do not hen create them using the Python make directory function
#a- ClippedKewx
#b-ExportedKewx

import os#import os to work with directories and folders
os.chdir('C:\EspinolaFinal')#change current working directory
dirname=["ClippedKEWX","ExportedKEWX"] #names of directories as a list

for dir in dirname:#iterate over directory list to create them if they don't already exist
    if not os.path.exists(dir):#Create target directory if don't exist
        os.mkdir(dir)#create directory
        print("Directory " , dir ,  " Created ")#print a message acknowledging creation of directory
    else:    
        print("Directory " , dir ,  " already exists")#print a seperate message if directory already exists
