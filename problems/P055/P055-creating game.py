import turtle 
pen = turtle.Turtle()
pen.penup() 
def pos(a) :
    return a * 35 

a = input("Enter the x and y and number of players (x , y , players) : ").split() 
x = int(a[0]) 
y = int(a[1]) 
player_names = int(a[2]) 
x1 = 1
while x1 <= y + 1 : 
    pen.pendown() 
    pen.fd(pos(x)) 
    pen.penup() 
    pen.goto(0 , pos(x1))
    x1 += 1
pen.goto(0 , 0) 
pen.left(90)  
y1 = 1 
while y1 <= x + 1 : 
    pen.pendown() 
    pen.fd(pos(y)) 
    pen.penup() 
    pen.goto(pos(y1) , 0) 
    y1 += 1 

the_input = str(input("START ? "))

class Player() :
    def __init__(self , Name , Blood , Position) : 
        a = 'Player' 