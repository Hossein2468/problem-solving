import turtle 

s = int(input("Enter the size of ground: "))
pencil = turtle.Turtle()
pencil.speed(3)
a = 0
b = 30 
while a < s :
    pencil.fd((s - 1) * 30)
    pencil.penup()
    pencil.goto(0 , b)
    pencil.pendown()
    a += 1 
    b += 30 
c = 0 
d = 30
pencil.penup()
pencil.goto(0 , 0)
pencil.left(90)
pencil.pendown()
while c < s :
    pencil.fd((s - 1) * 30)
    pencil.penup()
    pencil.goto(d , 0)
    pencil.pendown()
    c += 1 
    d += 30