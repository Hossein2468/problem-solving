question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    a = 1400 
    b = 1401 
if question == 'n' : 
    a = int(input("enter the first year: "))
    b = int(input("enter the second year: "))
a1 = (a * 365)
b1 = (b * 365)
c = (a1 - b1)
if (c < 0):
    print (f'{-c} days between {a} and {b}')
else:
    print (f'{+c} days between {a} and {b}')