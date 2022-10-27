n = int(input("Enter the number: "))
letters_list = []
words_list = []
for m in range(n):
    m = input("Enter the letters: ").split()
    letters_list.append(m)
o = " "
while o != "END" :
    o = input("Enter the words: ")
    words_list.append(o)
words_list.remove("END")

def position(a):
    from collections import namedtuple 
    pos = namedtuple('position' , ['y' , 'x'])
    

print(position(letters_list))