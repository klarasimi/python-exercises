'''
Takes two lists and finds their common elements without duplicates.
'''

import random

''' Function which takes two lists and finds elements which are common for them. If the elements is not on the new list, the function adds it.
'''

def find_common_numbers(list1, list2):
    common_elements = []
    for i in list1:
        if (i in list2) and (i not in   common_elements):
            common_elements.append(i)
    return common_elements

# Testing lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(find_common_numbers(a, b))

# Generating random lists
def generate_random_list():
    random_list = []
    for x in range(0, 10):
        random_list.append(random.randint(0, 10))
    return random_list

random_list1 = generate_random_list()
random_list2 = generate_random_list()

print("First random list is:",  random_list1)
print("Secodn random list is:",  random_list2)
print("They have these elements in common:", find_common_numbers(random_list1, random_list2))