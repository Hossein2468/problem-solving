import turtle 
def pos(a) :
    return a * 35

s = int(input("Enter the size of ground: ")) + 1
pencil = turtle.Turtle()
pencil.speed(5)
a = 1 
while a <= s :
    pencil.pendown()
    pencil.fd(pos(s - 1)) 
    pencil.penup()
    pencil.goto(0 , pos(a))
    a += 1 
pencil.penup()
pencil.left(90)
pencil.goto(0 , 0)
b = 1
while b <= s :
    pencil.pendown()
    pencil.fd(pos(s - 1))
    pencil.penup()
    pencil.goto(pos(b) , 0)
    b += 1 

g = input("Enter the gate position: ").split() 
g1 = list(map(lambda x : int(x) , g[0].split(',')))
g2 = list(map(lambda x : int(x) , g[1].split(',')))
gate = turtle.Turtle('turtle') 
gate.pencolor('blue')
gate.penup()
gate.goto(pos(g1[0]) , pos(g1[1]))
gate.pendown() 
gate.goto(pos(g2[0]) , pos(g2[1]))
gate1 = turtle.Turtle('turtle')
gate1.pencolor('blue')
gate1.penup()
gate1.goto(pos(g2[0]) , pos(g2[1]))
gate1.pendown() 
gate1.goto(pos(g1[0]) , pos(g1[1]))

b = input("Enter the ball position: ").split(',')
ball = list(map(lambda x : int(x) , b)) 
ball1 = turtle.Turtle('circle')
ball1.speed(1)
ball1.color('green')
ball1.penup()
ball1.goto(pos(ball[0]) , pos(ball[1]))

r = input("Enter the robot position: ").split(',') 
robot = list(map(lambda x : int(x) , r))
bot = turtle.Turtle('square')
bot.speed(1)
bot.color('cyan')
bot.penup()
bot.goto(pos(robot[0]) , pos(robot[1]))

