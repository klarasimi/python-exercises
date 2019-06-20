'''
Script which counts the ellipse content 
PyLadies Excercise from naucse.python.cz

date: 20-06-2019
'''

from math import pi

#Function with a calculation
def obsahElipsy(a, b):
    obsah = a * b * pi
    return obsah

a = int(input("Zadejte první osu: "))
b = int(input("Zadejte druhou osu: "))

# Call of a function 
obsah = obsahElipsy(a, b)

print("Obsah vaší elipsy je %s" % obsah)