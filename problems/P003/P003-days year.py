question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    a = 1400 
    b = 1401 
if question == 'n' : 

    a = int(input("enter the first year: "))
    b = int(input("enter the second year: "))
a = (a * 365)
b = (b * 365)
c = (a - b)
if (c < 0):
    print (-c)
else:
    print (+c)