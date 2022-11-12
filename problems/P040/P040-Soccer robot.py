import turtle 
def pos(a) :
    return a * 35

s = int(input("Enter the size of ground: ")) + 1
pencil = turtle.Turtle()
pencil.speed(7)
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
gate1 = turtle.Turtle('turtle') 
gate1.pencolor('blue')
gate1.penup()
gate1.goto(pos(g1[0]) , pos(g1[1]))
gate1.pendown() 
gate1.goto(pos(g2[0]) , pos(g2[1]))
gate2 = turtle.Turtle('turtle')
gate2.pencolor('blue')
gate2.penup()
gate2.goto(pos(g2[0]) , pos(g2[1]))
gate2.pendown() 
gate2.goto(pos(g1[0]) , pos(g1[1]))

b = input("Enter the ball position: ").split(',')
ball = list(map(lambda x : int(x) , b)) 
the_ball = turtle.Turtle('circle')
the_ball.speed(1)
the_ball.color('green')
the_ball.penup()
the_ball.goto(pos(ball[0]) , pos(ball[1]))

r = input("Enter the robot position: ").split(',') 
robot = list(map(lambda x : int(x) , r))
bot = turtle.Turtle('square')
bot.speed(1)
bot.color('cyan')
bot.penup()
bot.goto(pos(robot[0]) , pos(robot[1]))

def find_way_goal(g1 , g2 , ball , bot) :
    ball_distance1 = [g1[0] - ball[0] , g1[1] - ball[1]] 
    ball_distance2 = [g2[0] - ball[0] , g2[1] - ball[1]]
    if ball_distance1[0] > 0 and ball_distance2[0] > 0 :
        bot.goto(pos(ball[0] - 1) , pos(robot[1]))
        bot.goto(pos(robot[0]) , pos(ball[1] - 1))

print(find_way_goal(g1 , g2 , ball , bot))