question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    n = [23 , 45 , 1 , 89 , 100 , 2 , 31 , 345 , 67 , 70 , 20]
    o = 'ASC'
if question == 'n' : 
    n = input("Enter the numbers: ").split()
    o = input("Enter the sort form: ")
m = list(map(lambda x : int(x) , n))
p = []
for x in m :
    p.append(x)

def minimmum(a) : 
    b = 0 
    while b < len(a) : 
        c = a[b] 
        d1 = 0 
        for d in a : 
            if c <= d :
                d1 += 1 
                if d1 == len(a) :
                    return c 
        b += 1  
def maximum(a) : 
    b = 0 
    while b < len(a) : 
        c = a[b] 
        d1 = 0 
        for d in a : 
            if c >= d :
                d1 += 1 
                if d1 == len(a) :
                    return c 
        b += 1  

def ascending_and_descending(m , p):
    list1 = [] 
    a = 0 
    while a < len(p):
        if o == 'ASC':
            b = minimmum(m)
            list1.append(b)
            m.remove(b)
            a += 1
        if o == 'DESC':
            c = maximum(m)
            list1.append(c)
            m.remove(c)
            a += 1
    return list1 
print(ascending_and_descending(m , p))