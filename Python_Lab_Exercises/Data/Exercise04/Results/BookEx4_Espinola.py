# Name: David Espinola
#Date: February, 15, 2109
#Description: Lab 4




# Name: David Espinola
#Date: February, 13, 2109
#Description: Challenge 1-This script looks for occurence of letter in string and prints a messge to console depending on whether letter is in string or not


#Declare a string
letter= "Georaphic Information Systems"

#Use if statement to print two messages depending on if letter "z" is in string
if letter.find("z") !=-1: # note that find method return -1 if substring is not found in original string
    print "Yes"
else:
    print "No"


# Name: David Espinola
#Date: February, 13, 2109
#Description: Challenge 2 -This script looks for second largest number in list

numbers=[2,8,64,16,32,4]

#sort numbers in default ascending order
numbers.sort()

#print second from last number which will be second largest number
print numbers[-2]

# Name: David Espinola
#Date: February, 13, 2109
#Description: Challenge 3-This script looks for duplicate values in a list

numbers=[2,8,64,16,32,4,16,8]
numbers.sort()
duplist=[]

i=0

while i<len(numbers)-1:
    if numbers[i]==numbers[i+1]:#checks if next entry matches current entry in sorted list
        duplist.append(numbers[i])# create a list of duplicate values if desired
    i=i+1


#prints message about whether or not there is duplicates
if len(duplist)>0:
    print("List contains duplicate values"+str(duplist))
else:
    print("List does not contain duplicate values")

#Alternate code to print actual duplicates and to remove duplicates
for num in numbers:
    if numbers.count(num)!=1:
        numbers.remove(num)
        duplist.append(num)
        
#prints message about whether or not there is duplicates
if len(duplist)>0:
    print("List contains duplicate values"+str(duplist))
    
else:
    print("List does not contain duplicate values")


# Name: David Espinola
#Date: February, 15, 2109
#Description: Challenge 4-This script runs different list operations to determine result


mylist=["Athens", "Barcelona","Cairo","Florence","Helsinki"]

#part a returns the length of the list i.e. how many elements are in it
print(len(mylist))

#part b returns third element of the list
print(mylist[2])

#part c returns list elements starting at second element till the end of the list
print(mylist[1:])

#part d returns the last element of the list
print(mylist[-1])

#part e returns the number 2 which is index of list element "Cairo"
print(mylist.index("Cairo"))

#part f returns "Barcelona" and removes that element from the list
print(mylist.pop(1))

#part g sorts the list in descending order i.e. reverse alphabetical order
mylist.sort(reverse=True)
print(mylist)

#part h adds the city Berlin to the list
mylist.append("Berlin")
    






