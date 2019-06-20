'''
Script with a simple game where the player is supposed to get 21 points in order to win
PyLadies Excercise from naucse.python.cz

date: 20-06-2019
'''

from random import randrange

body = 0

# Drawing more cards
while body < 21:
    
    print("Máte ", body, "bodů.")
    odpoved = input("Chcete pokračovat? >> ")
    
    if odpoved == "ano":
        karta = randrange(2, 11)
        print("Otočili jste ", karta)
        body += karta
    
    elif odpoved == "ne":
        break

# Evaluation of the score
if body == 21:
    print("Gratulace! Vyhráli jste.")

elif body > 21:
    print("Smůla.")

else:
    print("Chybělo jen ", 21 - body, " bodů.")