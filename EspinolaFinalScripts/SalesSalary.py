#Question 2.1-SalesSalary.py:Salespersons work on commission, and their salary depends on the commission rate which is as follows"
#For sales greater or equal to 20,000 then rate=0.15
#For sales greater or equal to 15,000 then rate =0.10
#For other sales the rate=0.05
#In the class SalesSalary.py you must have:
#i)Class arguements:mySalary,mySales,myRate
#ii)Class methods:calcualteSalary,getSalary,getRate,setSales


class SalesSalary (object):# define the class sales salary 
     def __init__(self,mySales):
         self.mySales=mySales#sales will be the employee's sales
         self.myRate=0#initalize myRate.The rate will be calculated in calculateSalary method
         self.mySalary=0#initialize mySalary.The salary will be calculated in calculateSalary method
        
     def calculateSalary(self):#method of SalesSalary class used to calculate rate and salary based on employee sales all rates saved into self.myRate
         if self.mySales>=20000:
             self.myRate=0.15#if the sales are greater than or equal to 20,000 then the commission is 15%
         elif self.mySales>=15000:
             self.myRate=0.10#if the sales are greater than or equal to 15,000 then the commission is 10%
         else:
             self.myRate=0.05#if the sales are less than 15,000 the commission is 5%
             
         self.mySalary=int(self.myRate*float(self.mySales))#calculate the salary by multiplying commission rate by sales and save into self.mySalary
         #make sales a float so that myRate and mySales are both floating point numbers and Python won't give a data type error



    
    