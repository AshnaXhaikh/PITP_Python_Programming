"""This file imports the function and prints the student details."""
from school.student import student_info

"""use this if __init__.py imports the function"""
from school import student_info 

# Example student details
name = "Ashna Shaikh"
age = 18
grade = "12th"

# Call the imported function and print the result
details = student_info(name, age, grade)
print(details)


