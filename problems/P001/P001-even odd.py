question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    import random 
    h = random.randint(1 , 10) 
if question == 'n' : 
    h = int(input("enter the number:"))
if h % 2 == 0 :
    print (f"{h} is even.")
else:
    print (f"{h} is odd.")