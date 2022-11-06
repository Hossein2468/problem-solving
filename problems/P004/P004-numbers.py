question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    import random 
    a = random.randint(1 , 10)
if question == 'n' : 
    a = int(input("enter the number: "))
b = {1 : "one" , 2 : "two" , 3 : "three" , 4 : "four" , 5 : "five" , 6 : "six" , 7 : "seven" , 8 : "eight" , 9 : "nine" , 10 : "ten"}
print (b[a])