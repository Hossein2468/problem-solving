n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
q = list(map(lambda x : int(x) , p))
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
for c in set(q) :
    x = True 
    b = 0 
    while b < len(a) :
        d = a[b] 
        if c not in set(d) :
            x = False 
        b += 1 
    if x == True :
        print(c)