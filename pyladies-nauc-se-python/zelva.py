'''
Script which draws various patterns with Turtle Draw module
PyLadies Excercise from naucse.python.cz

date: 20-06-2019
'''

import turtle

# Change the arrow to a turtle
turtle.shape('turtle')

# Draws three slightly tilted squares starting from a one point
def kresliTriCtverce():
    
    for _ in range(0, 3):
    
        for _ in range(0, 4):
        
            turtle.forward(50)
            turtle.left(90)
    
        turtle.left(20)

# Draws a dashed line with gradualy longer dashes
def kresliPrerusovanouCaru():
    
    for i in range(0, 11):
    
        turtle.forward(5 + i)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

# Draws a set of stairs
def kresliSchody():
    
    for _ in range(0, 6):

        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)

# Draws six (or seven) hexagons
def kresliSestiuhelniky():
        
    for _ in range (0,6):    

        for _ in range(0, 6):
            turtle.forward(50)
            turtle.left(60)
    
        turtle.forward(50)
        turtle.right(60)

#kresliTriCtverce()
#kresliPrerusovanouCaru()
#kresliSchody()
kresliSestiuhelniky()

turtle.exitonclick()