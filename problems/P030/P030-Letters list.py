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
    positions = {}
    from collections import namedtuple 
    pos = namedtuple('position' , ['y' , 'x'])
    for b in range(len(a)) :
        b1 = a[b]
        for c in range(len(a[b])) :
            c1 = b1[c]
            d = pos(b + 1 , c + 1)
            positions.update({c1 : [d.y , d.x]}) 
    return positions

print(position(letters_list))