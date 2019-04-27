''' 
Program that asks for a number and prints out a list of all divisors.
'''

number = int(input("Insert a number: "))
divisors = []

# Finds out the divisors of a number
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i) # Appends the divisord to the list

print("Your number has these divisors:", divisors) # Prints out te list of divisors
