import turtle 
def pos(a) :
    return a * 40 

a = input("Enter the x and y and number of players (x , y , players) : ").split() 
x = int(a[0]) 
y = int(a[1]) 
player_names = int(a[2]) 

the_input = str(input("START ? "))

class Player() :
    def __init__(self , Name , Blood , Position) :
        self.Name =  Name
        self.Blood = Blood
        self.Position = Position 

import random  
n = 'Player'
players = [] 
for n1 in range(player_names) : 
    xpos = random.randint(2 , x)
    ypos = random.randint(2 , y)
    player = Player(f'{n}{n1 + 1}' , 10 , [xpos , ypos])
    players.append(player)
    position = player.Position
    bots = turtle.Turtle('square')
    bots.penup() 
    bots.color('red' , 'green')
    bots.goto(pos(position[0]) , pos(position[1]))
print(players)