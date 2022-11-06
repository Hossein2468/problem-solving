question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    a = 2 
    b = 3
    print('a =' , a)
    print('b =' , b) 
if question == 'n' : 
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
def my_sum(x , y): 
    return x + y
def my_subtract(x , y):
    return y - x 
def my_multiply(x , y):
    return x * y 
def my_divide(x , y):
    return y / x
print(my_sum(a , b))
print(my_subtract(a , b))
print(my_multiply(a , b))
print(my_divide(a , b))