# Name: David Matthew Espinola
# Date: February 13, 2019
# Description: This script demonstrates how to break a loop

from math import sqrt
for i in range(1001,0,-1):
    root=sqrt(i)
    if root==int(root):             #This evaluates whether the root is an integer
        print i
        break