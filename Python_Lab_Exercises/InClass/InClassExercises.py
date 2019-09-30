#In class exercises

#Exercise1,2-counting number of words in a string and letters in each individual word
a='How would you count the number of words in a string'
word_list=a.split(" ")# split string at space character and save into a list
for word in word_list:
    print(len(word))#traverse the list and count the letters in each word

print("The number of words in the list is "+str(len(word_list))+".")#find the number of element in the list which will be number of words in original string


#Exercise 3,4-Write a python code that prints first 100 odd numbers on a new line then on the same line.
odds=[]
for i in range (0,100):
    if i%2==1:#all odds will have remainder 1 when didvided by 2
        odds.append(i)#store the odds into a list so that they will print on same line when list is printed at the end of the loop
        print(i)
print(odds)#print all the odds from the odds list


#Exercise 5-String manipulation with a quote
quote="Ken Thompson once said, 'One of my most productive days was throwiing away 1000 lines of code'." #store a quote in a variable
print(quote)#print the quote
print(len(quote))#print the number of characters(including spaces in the quote).
spaces=quote.count(" ")#store number of spaces in variable spaces
print(spaces)#print number of spaces in quote
print(len(quote)-spaces)#print the number of non space character by subtracting total characters in space characters
print quote.isalpha()#prints are boolean true/false as to whether string has all alphabetical characters or not
quote_list=quote.split(" ")#put individual words of quote in a list
for word in quote_list:
    for character in word:
        if character.isalpha()==False:#check if each character in each word is an alphabet character. If it is not print message.
            print(str(word)+ " contains a none alphabet character")


#Exercise 6-Store your first name in a variable and print it in lowercase,uppercase and titlecase
name='david'#store my first name in a variable
print(name)#print name in lowercase
print(name.title())#print name in titlecase
print(name.upper())#print name in uppercase


#Exercise 7.1- Store first name and last name in seperate variable and combine to print full name
first_name='david'#store first name in a variable
last_name='espinola'#store last name in a variable
print(first_name.title()+" "+last_name.title())
#Exercise 7.2 Split the string 'Linus Torvalds' into two parts
linux_founder='Linus Torvalds'#store the string Linus Torvalds in a variable
split_founder=linux_founder.split(" ")#split the string at the space character
print(split_founder)#print the list with the broken up string
#Exercise 7.3 Split the list veggies="peas,green beans,spinach,corn,squash"
veggies="peas,green beans,corn,squash"#store the veggies string in a variable
veggies_list=veggies.split(",")#split the veggies string based on the comma
print(veggies_list)#print the veggies list

#Exercise 8- Store a person's first name and last name in seperate variables. Use concatentation to make a sentence about this person, and store sentence in a variable then print.
first_name='albert'#store first name in a variable
last_name='espinola'#store last name in a variable
sentence=first_name.title()+" "+last_name.title()+" lives in Katy, Texas."#store a sentence using concatenation about this person
print(sentence)#print the sentence

#Exercise 9-Store your name in a variable and include two types of whitespace. Print your name as its stored. Print your name with whitespace stripped from left side,right side,then both sides.
name_spaces="   David   "#store name with two types of whitespace on both sides
print(name_spaces)#print name with whitespace on both sides
print(name_spaces.lstrip())#print name with whitespace stripped from left side of name
print(name_spaces.rstrip())#print name with whitespace stripped from right side of name
print(name_spaces.strip())#print name with whitespace stripped from both sides of name

#Exercise 10-write a program that prints out the results of at least one calculation for each of the basic opeartions:addition,subtraction,multiplication,division
print(1+1)#print out the result of an addition problem
print(1-1)#print out the result of subtraction problem
print(1*1)#print out the result of multiplication problem
print(1/1)#print out the result of a division problem
print(1**2)#print out the resul tof an exponentiation problem

#Exercise 11-find a calculation that depends on the order of operations then print using standard order of operations then using parentheses to force nonstandard order of operations
print(2+3*5)#print calculation using standard order of operations
print((2+3)*5)#print calculation forcing nonstandard order of operations

#Exercise-12 Write a program which will find all such numbers which are divisible by 7 but not a multiple of 5,between 20 and 40(inclusive). The numbers should be printed in a comma seperated sequence on a single line.
divisible_list=[]# create empty list to hold numbers that meet criteria
for i in range(20,41):#loop through numbers 20 to 40
    if i %7==0 and i%5 !=0:#check if number is divisible by 7 or a multiple of 5
        divisible_list.append(i)# add numbers that meet this criteria to the list
print(divisible_list)        #print the list

#Exercise 13- Given a string,s,return a string made of the first 2 and last 2 characters of the original string.If string is less than 2 return empty string
old_string="spring"#string to be manipulated
new_string=""#empty string that holds result of manipulation
if len(old_string)<2:#test to see if string is less than 2 chars lon
    print(new_string)#print an empty string
else:
    new_string=old_string[0:2]+old_string[-2:]#slice string with first two chars and last 2 chars and concatenate the result
    print(new_string)#print the result in new string

#Exercise 14-return a function that finds the max of 3 numbers
max_list=[1,2,3]#list of three numbers
max=0#initialize max to a number for comaprison in loop
for num in max_list:#loop through list of numbers
    if num>max:#check if current number is greater than what is currently stored in max
        max=num#if current number is larger than max replace max with that number otherwise keep current max
print(max)   #print max after iterating through the list

#Exercise 15 write a python function to sum all the numbers in a list
vals=[0,2,4,8,16,18,17,14,9,7,4,2,1]#create a list of numbers to sum
total=0# initiate are a variable total that will hold sum of values in the list
for val in vals:#create for loop to iterate over values in list
    total=total+val#add current value in list to previous total and resave in total variable
print(total)#print total after completing the loop


#Exercise 16- write a python function to multiply all the numbers in a list
vals=[0,2,4,8,16,18,17,14,9,7,4,2,1]
product=1#initalize to 1 so that on first iteration you will store first number in the list as the product
for val in vals:
    product=product*val#multiply previous product times next value in list to get new product and store it in product
print(product)

#Exercise 17- Write a program to reverse a string
string="abcde123"#sample string
rev_string=""
for i in range(1,len(string)+1):
    rev_string=rev_string+string[-i]
print rev_string


#Exercise 18- Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters

def counter_case(samp_string):#function header. We are calling the function counter_case and its argument is a single string
    upper=0#initalize variable to hold number number of upper case letters
    lower=0#initialze variable to hold number of lower case letters
    for letter in samp_string:#create a loop to iterate over all the characters of the string
        if letter.isupper():#test if character is upper case with .isupper() method
            upper=upper+1#add 1 to counter variable if letter is upper case
        elif letter.islower():#test if character is lower case with .islower()method
            lower=lower+1#add 1 to counter variable if letter is lower case
    print("The number of lower case letters is " +str(lower) +" and the number of upper case letters is "+str(upper)) #return for function is statement with number of upper and lower case letters

#Exercise 19 Write a python function that takes a list and returns a new list with unique elements of the first list
def unique_list(samp_list):#function header. We are calling the function unique_list and its arguement is a single list
    new_list=[]#initialize an empty list to hold unique elemnts from first list
    for num in samp_list:#iterate over elements of first list
        if num not in new_list:#check if element is not new_list
            new_list.append(num)#if it is not in new_list add it
    return(new_list)#return the filled new_list

#Exercise 25-Write a program that can compute the factorial of a given number
def fact_fun(num):#function header. We are calling the function fact_fun and its arguement is an integer
    fact=1#initialize multiplier variable to one
    if num<0:#check to make sure number is positive
        print("factorial is undefined")#print an error if number is not positive
    elif num=0:#check if number is 0
        fact=1#zero factorial is defiined to be one
    else:    
        for i in range(1,num+1):#iterate over the number between 1 and the integer
            fact=fact*i#multiply each number by the product of the previous numbers and store in fact variable
return fact #return fact variable


#Exercise 28-Given a string,if its length is at least 3, add 'ing' to the end unless it ends in 'ing' then add 'ly' instead. If the string is less than 3,leave it unchanged.
old_string="test"#create a string to be manipulated
new_string=""#create a variable to hold manipulated string
if len(old_string)<3:#check if the string length is less than 3
    new_string=old_string#if it is leave the string alone 
    print(new_string)#print string
elif old_string[-3:]=='ing':#if the string is at least 3 chars long and ends in 'ing' add 'ly' to the end
    new_string=old_string+"ly"#save new string as old string with "ly" at the end
    print(new_string)#print new string
else:
    new_string=old_string+"ing"#if string if longer than 3 chars and does not end in 'ing' add and 'ing' to the end
    print(new_string)#print new string
    
    
    
    
        
        
        
