# Name: David Espinola
#Date: March, 20, 2019
#Description: Question 1

import math
for i in range(30,41):#iterate over numbers 30 through 40 inclusive
    print("Number is "+str(i)+" square root is = "+str(math.sqrt(i)))#print number and its square root

# Name: David Espinola
#Date: March, 20, 2019
#Description: Question 2
even_list=[]#create an empty list to store the even numbers
for i in range(0,21):#iterate over numbers from 0 to 20
    if i%2==0:#check that number is even i.e. zero remainder when divided by 2
        even_list.append(i)#if number is even add to evens_list
        print("number "+ str(i)+ " is even")#print the even numbers with message

# Name: David Espinola
#Date: March, 20, 2019
#Description: Question 3

for i in range(0,100):#iterate through numbers from 0 to 99
    if (i%8==0 and i%5==0):#check that number is divisible by 5 and 8
        print("number "+str(i)+ " is divisible by 8 and a multiple of 5")#print all the numbers that meet the condition with message

# Name: David Espinola
#Date: March, 20, 2019
#Description: Question 4

letters=['d','e','f','g','h','i','j','k','l','m','n','o','p']#create letter list
vowels=['a','e','i','o','u']#create vowel list

for letter in letters:#loop over letters in letter list
    if letter in vowels:#check if letter is a vowel using in operator
        print(letter+" is a vowel from letters list")#print letters that are vowels with message

# Name: David Espinola
#Date: March, 20, 2019
#Description: Question 5

nums=[12,67,1,89.0,3,0.8,23,65.9,34.62,64,98,12.3,27,6,14.2]#test number list

def nums_fun(num_list):#define function
    counter=0#iniitalize variable to count numbers less than 70
    nums_lt70=[]#create empty list to put numbers in that are less than 70

    for num in num_list:#iterate over number list passed to function
        if (type(num) is int and num<70):#check that number is an integer and less than 70
            counter=counter+1#add 1 to counter to keep count of numbers less than 70
            nums_lt70.append(num)#add number to the list
        
    print("Number of elements below 70 is: "+str(counter))#print number of elements that were integers below 70
    print("The values of the elements are:"+str(nums_lt70))#print the values of elements below 70
    return#return statement to close function
        


    