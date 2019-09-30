#Class exercise 1
##a=[1,4,8,12]
##b=20
##for i in range(len(a)):
##    if b-a[i] in a:
##        print "here is i",i,"here is b",b,"difference will be",b-a[i]
##
##
##
##for i in range(1,29):
##    if math.sqrt(i)%1==0:
##         print "this is i {0} and this is sqrt {1}".format(i,math.sqrt(i))

        
###Class exercise 2
##import math         
##def least_squares(num):
##    perfect_squares=[0,1]
##    counter=0
##    while len(perfect_squares)>0:
##        if counter==0:
##            count=0
##        if num>0:
##            perfect_squares=[]
##            for i in range(1,num):
##                if math.sqrt(i) is int:
##                    perfect_squares.append(i)
##            if len(perfect_squares)>0:        
##                largest_ps=max(perfect_squares)
##                num=num-largest_ps
##                count=count+1
##    counter=counter+1           
##    print(count)       
##    return count




#Class exercise 2
import math         
def least_squares(num):
    count=0
    
    while num>0:
        perfect_squares=[]
        for i in range(1,num):
            if math.sqrt(i) is int:
                perfect_squares.append(i)
            if len(perfect_squares)>0:        
                largest_ps=max(perfect_squares)
                num=num-largest_ps
                count=count+1          
                print(count)       
    return count



