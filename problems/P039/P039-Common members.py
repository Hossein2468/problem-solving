n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
q = list(map(lambda x : int(x) , p))
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
b = 0 
while b < len(a) :
    c = a[b] 
    for d in q :
        if d in c :
            b += 1 
    print(d)