# Name: David Espinola
#Date: February, 15, 2109
#Description: This script runs different list operations to determine result


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
