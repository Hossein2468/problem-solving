question = str(input("Do you like to run with sample input? (y/n): "))
if question == 'y' : 
    text = 'P:James Webb will change our understanding of universe'
if question == 'n' :
    text = input("Enter the text: ")

lits = {'A' : '4' , 'B' : '8' , 'C' : '(' , 'D' : '|)' , 'E' : '3' , 'F' : '|=' , 'G' : '6' , 'H' : '}{' , 'I' : '1' , 'J' : '_7' , 'K' : '|<' , 'L' : '|_' , 'M' : '44' , 'N' : '/\/' , 'O' :'0' , 'P' : '|*' , 'Q' : '9' , 'R' : '12' , 'S' : '5' , 'T' : '-|-' , 'U' : '(_)' , 'V' : '\/' , 'W' : '\/\/' , 'X' : '*' , 'Y' : '\|/' , 'Z' : '2'}
sentence = [] 
if text.startswith('P') : 
    a = text[2:].split()
    b = 0 
    while b < len(a) : 
        u = []
        u1 = 0
        c = a[b].upper() 
        while u1 < len(c) : 
            d = c[u1]
            u.append(lits[d])
            u1 += 1 
        b += 1 
        sentence.append(' '.join(u)) 
    print('Encrypted Text is :' , '  '.join(sentence))

if text.startswith('E') : 
    def invert_dictionary(dict1):
        return {v: k for k, v in dict1.items()}
    lits1 = invert_dictionary(lits) 
    a = text[2:].split('  ')
    b = 0 
    while b < len(a) : 
        u = [] 
        u1 = 0 
        c = a[b].split(' ')
        while u1 < len(c) : 
            d = c[u1]
            u.append(lits1[d])
            u1 += 1 
        b += 1 
        sentence.append(''.join(u)) 
    print('Plain text is :' , ' '.join(sentence).lower())