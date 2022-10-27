n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
q = list(map(lambda x : int(x) , p))
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
numbers = {'a'}
for b in a :
    for c in b :
        if c in q :
            numbers.add(c)
numbers.remove('a')
print(numbers)