#Question 4.2- Write a section of code to define a function 'Student',where each student should have two data instances(arguments),one for the student's name,
#and one for the student numerical final grade. The Student function,should have the method 'ConvertGrade', which should return the letter grade for the student
#following the rules below:
#a). for students with final grade no less than 95,return 'A';
#b). for students with final grade less than 95 but no less than 80,return 'B';
#c). for students with final grade less than 80 but no less than 65,return 'C';
#d). for students with final grade less than 65 but no less than 55, return 'D';
#e). otherwise,return 'F'.


def Student(num_grade,name='John Doe'):#create student function with numerical grade and student name as arguements
    if num_grade>=95:
        letter_grade='A'#grades greater than or equal to 95 are an 'A'
    elif num_grade>=80:
        letter_grade='B'#grades greater than or equal to 80 and less than 95 are a 'B'
    elif num_grade>=65:
        letter_grade='C'#grades greater than or equal to 65 and less than 80 are a 'C'
    elif num_grade>=55:
        letter_grade='D'#grades greater than or equal to 55 and less than 65 are a 'D'
    else:
        letter_grade='F'#all grades loweer than 55 are an 'F'
    return letter_grade
