#Question 4.1-Write a code for the simple program "UserString.py" which will read a string from the keyboard and print it out on the screen,
#you should test that the user input is only Alphabetical. The code should be a complete program that can run;that is
#if the user uses numbers and/or other characters non alphabetical,your code should print back to the screen
# "Wrong input,please try again". If the user input is strictly alphabetical then print it to the screen with a simple message.



test_string=raw_input("Please enter a text string.")#Get string from the user via popup box
if test_string.isalpha():#check that the string is only alphabetical
    print" The string you entered is: " + test_string#print the string if it is only alphabetical
else:
    print "Wrong input,please try again."   #print an error message if the string is not alphabetical 