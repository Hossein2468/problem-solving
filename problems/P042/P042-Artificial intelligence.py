import turtle
my_pen = turtle.Turtle()
my_pen.speed(1)

def pos(x) :
    a = x * 35 
    return a 

n = input("Enter the positions: ").split(')')
n1 = n[0]
n2 = n[1]
me_1 = list(map(lambda x : int(x) , n1[1:].split(',')))
the_target = list(map(lambda x : int(x) , n2[1:].split(',')))
m = int(input("Enter the number of obstacles: "))
obstacles = []
for m1 in range(m):
    m1 = input("Enter the obsracles: ").split(')')
    m2 = 0 
    obstacles1 = []
    while (m2 + 1) < len(m1) :
        m3 = m1[m2] 
        m4 = list(map(lambda x : int(x) , m3[1:].split(',')))
        obstacles1.append(m4)
        m2 += 1
    obstacles.append(obstacles1)
ob = 0 
my_pen.penup()
while ob < len(obstacles) :
    ob1 = obstacles[ob] 
    st = 1 
    my_pen.goto(pos((ob1[0])[0]) , pos((ob1[0])[1]))
    while st < len(ob1) :
        st1 = ob1[st] 
        my_pen.pendown()
        my_pen.goto(pos(st1[0]) , pos(st1[1]))
        st += 1 
    my_pen.penup()
    ob += 1 
me = turtle.Turtle('circle')
me.color('green')
me.penup()
me.speed(1)
target = turtle.Turtle('circle')
target.color('red')
target.penup()
target.speed(1)
me.goto(pos(me_1[0]) , pos(me_1[1]))
me.pencolor('blue')
target.goto(pos(the_target[0]) , pos(the_target[1]))

distance = [the_target[0] - me_1[1] , the_target[1] - me_1[1]] 