''' 
Takes a list and prints out all numbers lees than 5.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = [] 

for i in a: # Finds numbers lower than 5
    if i < 5:
        # print(i)
        less_than_5.append(i) # Adds the numbers to the new list

print(less_than_5) # Prints out the new list

print("Now let's try again with your number. Insert 10 numbers.")

user_list = []

for i in range(10): # Goes through the user's list and compares the numbers with 5, prints out lower numbers.
    user_number = int(input("> "))
    if user_number < 5:
        user_list.append(user_number)

print(user_list)