"""
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""
#The below code will ask the user to provide the name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
#This below code will use the name and creating the personalized message to the user
message = "Hello, " + first_name + " " + last_name + "! " + "Welcome to the python program."
#printing the message to the user
print(message)
