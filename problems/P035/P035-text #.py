sentences = []
words = []
while True :
    a = input("Enter the sentences: ")
    if a == "END" :
        break 
    sentences.append(a)
b = 1
while b < len (sentences) :
    c = sentences[0]
    d = sentences[b] 
    c1 = 0
    while c1 < len(c) : 
        for c2 in range(c1 , len(c) + 1) : 
            c3 = c[c1 : c2] 
            d1 = 0 
            while d1 < len(d) : 
                for d2 in range(d1 , len(d) + 1) :
                    d3 = d[d1 : d2] 
                    if c3 == d3 and c3 != ' ' and c3 != '' and c[0] != ' ' and c3[-1] != ' ' : 
                        words.append(c3) 
                d1 += 1 
        c1 += 1 
    b += 1
e = list(map(lambda x : len(x) , words))
e1 = e.index(max(e)) 
word = words[e1] 
index = [] 
for i in sentences : 
    index.append(i.index(word)) 
i1 = max(index) 
i2 = 0 
while i2 < len(sentences) :
    sentence = sentences[i2] 
    if sentence.index(word) < i1 : 
        u = i1 - sentence.index(word) - 1
        o = sentence.split() 
        o.insert(0 , '#' * u)
        print(' '.join(o)) 
    else : 
        print(sentence)
    i2 += 1