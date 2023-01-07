hw = input("Enter the 'W' and'H' : ").split()
wh = list(map(lambda x : int(x) , hw))
n = int(input("Enter the number of stars: "))
stars = {} 
for n1 in range(n) :
    n2 = input("Enter the stars names: ").split()
    stars.update({n2[0] : [int(n2[1]) , int(n2[2])]})
my_position = input("Enter my Position (x , y) : ").split()
pos = list(map(lambda x : int(x) , my_position))
target = str(input("Enter the star target: ")) 
light_sec = 300000000

def fisaghores(a1 , b1) :
    c1 = (a1 ** 2) + (b1 ** 2) 
    au = 150000000000
    return (c1 ** (1 / 2)) * au

a11 = stars[target] 
b11 = [abs(a11[0] - pos[0]) , abs(a11[1] - pos[1])]
c11 = fisaghores(b11[0] , b11[1])
d11 = (c11 / light_sec)
print(f'{target} : {d11} seconds')
stars.pop(target)

while stars != {} :
    distance = [] 
    for a in stars :
        b = stars[a] 
        c = [abs(a11[0] - b[0]) , abs(a11[1] - b[1])]
        distance.append(c[0] + c[1]) 
    d = min(distance) 
    for e in stars :
        f = stars[e]
        u = (abs(a11[0] - f[0]) + abs(a11[1] - f[1])) 
        if u == d :
            g = fisaghores(f[0] , f[1]) 
            h = (g / light_sec)
            print(f'{e} : {h} seconds')
            a11 = stars[e]
            target = e 
            stars.pop(target)
            break 