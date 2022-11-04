n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
q = list(map(lambda x : int(x) , p))
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
for c in set(q) :
    x = 1 
    for d in a :
        if c in set(d) :
            x += 1  
    if x == n : 
        print(c) 