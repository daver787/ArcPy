#Question 4.2.2-Write a section of code called "StudentGrade.py" to implement the function,use the following grades for testing (97,83,71,60 and 54)
import ConvertGrade#import your script with the Student function
grade_list=[97,83,71,60,54]#create a list of all the test grades

for grade in grade_list:#loop through the list of test grades
    print(ConvertGrade.Student(grade))#print the letter grade and student name for each grade using the imported Student function