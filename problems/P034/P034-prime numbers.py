n = int(input("Enter the number: "))

def prime_number_list(n):
    numbers = []
    a = str(n)
    b = 0 
    while b < len(a):
        for c in range((b + 1) , (len(a) + 1)):
            d = a[b : c]
            numbers.append(int(d))
        b += 1
    return list(set(numbers))

r = prime_number_list(n)

def is_prime(r):
    myset = {"a"}
    for a in r :
        for x in range(2 , a):
            if a % x == 0 :
                myset.update({a})
    myset.remove("a")
    for i in myset:
        r.remove(i)
    for t in r :
        if t == 1:
            r.remove(1)
    for s in r :
        if s == 0:
            r.remove(0)
    return set(r)     

print(is_prime(r))