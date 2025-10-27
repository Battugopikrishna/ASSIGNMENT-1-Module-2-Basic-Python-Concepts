"""
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""
#This code will ask the user to provide the values to perform calculation
value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))

#the below code will work on the calculation
Addition = value1 + value2
Subtraction = value1 - value2
Multiplication = value1 * value2
Division = value1 / value2

# the below code will provide the output to user with the results
print("Addition: ", Addition)
print("Subtraction: ", Subtraction)
print("Multiplication: ", Multiplication)
print("Division: ", Division)
