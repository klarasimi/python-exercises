''' 
Program asks the user to enter their name and their age. 

Prints out a message addressed to the user and tells them the year that they will turn 100 years old.
'''

import datetime

name = input("Enter your name: ")
age = input("Enter you age: ")

if int(age) < 0:
    print("You have not been born yet.")
    exit()
else:
    now = datetime.datetime.now() 
    current_year = now.year # Finds out the current year

    century = current_year + (99 - int(age)) # Calculates the 100th birthday

    print("Hi", name, "! Today you are", age, "and you will turn 100 years in", century) # Prints the answer

number_of_copies = input("How many times would you like to print the answer? ")

# Prints copy of the final message so many times user wants
for i in range(0, int(number_of_copies)):
    print("Hi", name, "! Today you are", age, "and you will turn 100 years in", century)