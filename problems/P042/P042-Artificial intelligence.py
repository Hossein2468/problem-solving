import turtle
my_pen = turtle.Turtle()
my_pen.speed(1)

def pos(x) :
    a = x * 35 
    return a 

question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    me_1 = [4 , 2]
    the_target = [7 , 9]
    obstacles = [[[2 , 1] , [2 , 2] , [3 , 2] , [3 , 3] , [4 , 3] , [5 , 3] , [5 , 2] , [6 , 2] , [7 , 2]] , [[7 , 4] , [7 , 3] , [8 , 3]] , [[10 , 2] , [10 , 3] , [10 , 4] , [10 , 5] , [10 , 6] , [9 , 6] , [8 , 6] , [7 , 6]] , [[7 , 7] , [6 , 7] , [6 , 6] , [5 , 6]] , [[3 , 5] , [3 , 6] , [4 , 6]] , [[4 , 8] , [3 , 8] , [3 , 9] , [4 , 9] , [5 , 9] , [5 , 10]]]
if question == 'n' :
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
target.color('blue')
target.penup()
target.speed(1)
me.goto(pos(me_1[0]) , pos(me_1[1]))
me.pencolor('blue')
target.goto(pos(the_target[0]) , pos(the_target[1]))

distance = [the_target[0] - me_1[0] , the_target[1] - me_1[1]] 
def hi(a , b , c , distance) :
    the_way = [me_1]
    lost_ways = [] 
    while distance != [0 , 0] :
        if distance[0] > 0 and distance[1] > 0 : 
            a1 = [a[0] + 1 , a[1]] 
            a2 = [a[0] , a[1] + 1] 
            a3 = [a[0] - 1 , a[1]] 
            a4 = [a[0] , a[1] - 1] 
        if distance[0] < 0 and distance[1] < 0 :
            a1 = [a[0] - 1 , a[1]] 
            a2 = [a[0] , a[1] - 1]
            a3 = [a[0] + 1 , a[1]] 
            a4 = [a[0] , a[1] + 1]
        if distance[0] > 0 and distance[1] < 0 :
            a1 = [a[0] + 1 , a[1]] 
            a2 = [a[0] , a[1] - 1]
            a3 = [a[0] - 1 , a[1]] 
            a4 = [a[0] , a[1] + 1]
        if distance[0] < 0 and distance[1] > 0 :
            a1 = [a[0] - 1 , a[1]] 
            a2 = [a[0] , a[1] + 1]
            a3 = [a[0] + 1 , a[1]] 
            a4 = [a[0] , a[1] - 1] 
        if distance[0] > 0 and distance[1] == 0 :
            a1 = [a[0] + 1 , a[1]] 
            a2 = [a[0] , a[1] + 1]
            a3 = [a[0] - 1 , a[1]] 
            a4 = [a[0] , a[1] - 1] 
        if distance[0] < 0 and distance[1] == 0 :
            a1 = [a[0] - 1 , a[1]] 
            a2 = [a[0] , a[1] - 1] 
            a3 = [a[0] + 1 , a[1]] 
            a4 = [a[0] , a[1] + 1]
        if distance[0] == 0 and distance[1] > 0 :
            a1 = [a[0] , a[1] + 1] 
            a2 = [a[0] + 1 , a[1]] 
            a3 = [a[0] , a[1] - 1] 
            a4 = [a[0] - 1 , a[1]]
        if distance[0] == 0 and distance[1] < 0 :
            a1 = [a[0] , a[1] - 1] 
            a2 = [a[0] - 1 , a[1]] 
            a3 = [a[0] , a[1] + 1] 
            a4 = [a[0] + 1 , a[1]]
        x1 = True 
        x2 = True 
        for d1 in c :
            for e1 in d1 :
                if a1 == e1 :
                    x1 = False 
                if a2 == e1 :
                    x2 = False  
        if x1 == True :
            x1 = False
            if a1 not in the_way and a1 not in lost_ways :
                the_way.append(a1) 
                distance = [b[0] - a1[0] , b[1] - a1[1]]
                a = a1 
                x1 = True 
        if x2 == True and x1 == False :
            x2 = False 
            if a2 not in the_way and a2 not in lost_ways :
                the_way.append(a2) 
                distance = [b[0] - a2[0] , b[1] - a2[1]]
                a = a2 
                x2 = True 
        if x1 == False and x2 == False :
            x3 = True 
            x4 = True 
            for d2 in c :
                for e2 in d2 :
                    if a3 == e2 :
                        x3 = False 
                    if a4 == e2 :
                        x4 = False 
            if x3 == True :
                x3 = False
                if a3 not in the_way and a3 not in lost_ways :
                    the_way.append(a3) 
                    distance = [b[0] - a3[0] , b[1] - a3[1]]
                    a = a3
                    x3 = True  
            if x4 == True and x3 == False:
                x4 = False
                if a4 not in the_way and a4 not in lost_ways :
                    the_way.append(a4) 
                    distance = [b[0] - a4[0] , b[1] - a4[1]]
                    a = a4 
                    x4 = True 
        if x1 == False and x2 == False and x3 == False and x4 == False and len(the_way) : 
            lost = the_way[-1] 
            lost_ways.append(lost) 
            the_way.remove(lost)
            if len(the_way) != 0 :
                lost = the_way[-1] 
                distance = [b[0] - lost[0] , b[1] - lost[1]]
                a = lost
            if len(the_way) == 0 : 
                return 'IMPOSSIBLE' 
    return the_way

hello = hi(me_1 , the_target , obstacles , distance)
me.pendown()
me.speed(1)
print(hello)
if hello != 'IMPOSSIBLE' :
    for way in hello :
        me.goto(pos(way[0]) , pos(way[1]))