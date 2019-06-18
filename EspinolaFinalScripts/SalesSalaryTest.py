#Question 2.2-In SalesSalaryTest.py,you must:
#i)Ask user to input the sales amount, should be a double value, from keyboard;
#ii)If the sale amount is a positive number(this means you need to test it),create an object of class SalesSalary,calculate the salary and print out the information
#(sale amount commission rate, and salary)
#iii)If the sale amount is a negative number, print out the message "invalid sale amount".
from SalesSalary import *#import the salesSalary class
mySales=float(raw_input("Please enter a sales amount"))#prompt the user for the sales of the employee
if mySales<0:# if the sales are negative(invalid amount) print an error message of invalid sales amount
    print "invalid sale amount"
else:
    testSales=SalesSalary(mySales)#otherwise create instantiate the testSales object,passing it the sales amount,mySales
    testSales.calculateSalary()#call the calculateSalary method of test to calcualte the rate and salary for the employee
    print "Sales amount: "+str(testSales.mySales)#print the sales amount back to console
    print "Commission rate: "+str(testSales.myRate)#print the commission rate back to the console
    print "Salary: "+str(testSales.mySalary)#print the salary back to the console



#When testing your program,you should input the following values and copy the output to here;
#i). -12000;
#ii). 10000;
#iii). 18000;
#iv). 30000;    
##output from test data
##
##invalid sale amount
##>>> Sales amount: 10000
##Commission rate: 0.05
##Salary: 500
##Sales amount: 18000
##Commission rate: 0.1
##Salary: 1800
##Sales amount: 30000
##Commission rate: 0.15
##Salary: 4500