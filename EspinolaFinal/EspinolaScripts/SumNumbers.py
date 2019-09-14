#Question 4.3- Write a section of code to compute the summation of all integer numbers between 10 and 20(inclusive). You need to use the while-loop.

i=10#initialize your number variable,i
sum=0#create a variable sum to accumulate the sum calculated in the loop.

while i<21:#test condition that executes the loop only if the number,i,is less than 21
    sum=sum+i#add the value of your number i to the current sum
    i=i+1#add 1 to your number until it reaches 20
print sum   #print the sum of the numbers from 10 to 20 after the loop is finished calculating the sum 
    