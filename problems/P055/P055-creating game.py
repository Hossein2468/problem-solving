import turtle 
pen = turtle.Turtle()
pen.speed(6)
pen.penup() 
def pos(a) :
    return a * 40 

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
        self.Name =  Name
        self.Blood = Blood
        self.Position = Position 

import random  
n = 'Player'
for n1 in range(player_names) : 
    xpos = random.randint(2 , x)
    ypos = random.randint(2 , y)
    player = Player(f'{n}{n1 + 1}' , 10 , [xpos , ypos])
    position = player.Position
    bots = turtle.Turtle('square')
    bots.penup() 
    bots.color('red' , 'green')
    bots.goto(pos(position[0]) , pos(position[1]))
print(player.Name)