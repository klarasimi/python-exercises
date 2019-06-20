from random import randrange

body = 0

while body < 21:
    
    print("Máte ", body, "bodů.")
    odpoved = input("Chcete pokračovat? >> ")
    
    if odpoved == "ano":
        karta = randrange(2, 11)
        print("Otočili jste ", karta)
        body += karta
    
    elif odpoved == "ne":
        break

if body == 21:
    print("Gratulace! Vyhráli jste.")

elif body > 21:
    print("Smůla.")

else:
    print("Chybělo jen ", 21 - body, " bodů.")