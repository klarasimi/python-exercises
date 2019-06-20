import turtle

turtle.shape('turtle')

def kresliTriCtverce():
    
    for _ in range(0, 3):
    
        for _ in range(0, 4):
        
            turtle.forward(50)
            turtle.left(90)
    
        turtle.left(20)

def kresliPrerusovanouCaru():
    
    for i in range(0, 11):
    
        turtle.forward(5 + i)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

def kresliSchody():
    
    for _ in range(0, 6):

        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)

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