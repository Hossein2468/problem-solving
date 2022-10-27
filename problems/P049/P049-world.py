hw = input("Enter the 'W' and'H' : ").split()
wh = list(map(lambda x : int(x) , hw))
n = int(input("Enter the number of stars: "))
stars = {} 
for n1 in range(n) :
    n2 = input("Enter the stars names: ").split()
    stars.update({n2[0] : [int(n2[1]) , int(n2[2])]})
my_position = input("Enter my Position: ").split()
pos = list(map(lambda x : int(x) , my_position))
target = str(input("Enter the star target: ")) 