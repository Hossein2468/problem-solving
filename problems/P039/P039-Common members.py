question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    n = 5
    p = ['3' , '90' , '4' , '1' , '67' , '59' , '2']
    a = [['4' , '67' , '32' , '2' , '90' , '4'] , ['4' , '90' , '3' , '1' , '56' , '387' , '34' , '2'] , ['2' , '67' , '532' , '876' , '90'] , ['4' , '29' , '61' , '39' , '2' , '90']]
if question == 'n' : 
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