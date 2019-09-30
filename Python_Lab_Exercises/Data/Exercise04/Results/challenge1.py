# Name: David Espinola
#Date: February, 13, 2109
#Description: This script looks for occurence of letter in string and prints a messge to console depending on whether letter is in string or not


#Declare a string
letter= "Georaphic Information Systems"

#Use if statement to print two messages depending on if letter "z" is in string
if letter.find("z") !=-1: # note that find method return -1 if substring is not found in original string
    print "Yes"
else:
    print "No"