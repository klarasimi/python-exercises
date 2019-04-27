''' 
Program asks user for a number. Finds out if the number is odd or even and prints out the message.
'''

# Asks the user for input
number = int(input("Type a number: ")) 

# Compares the modulo
if number % 4 == 0:
    print("I was told to print different message when the number is a multiple of 4. Here it is.")
elif number % 2 == 0: 
    print("You entered even number.")
elif number % 2 == 1:
    print("You entered odd number.")
else:
    print("Well, that was unexpected.")

# Asks for the input of two other numbers
num = int(input("Now enter another number: "))
check = int(input("And a number you want to divide it by: "))

# And finds out, if the "num" evenly divides by "check"
if num % check == 0:
    print("Congratulations,", check, "evenly divides", num, ".")
else:
    print(check, "doesn't evenly divide", num, ". Better luck next time.")