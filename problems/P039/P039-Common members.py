n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    a.append(m)
for c in set(p) :
    x = 1 
    for d in a :
        if c in set(d) :
            x += 1  
    if x == n : 
        print(c) 