sentences = []
word = []
while True :
    a = input("Enter the sentences: ").split()
    if a == ["END"] :
        break 
    sentences.append(a)
b = 1
while b < len (sentences) :
    c = sentences[0]
    d = sentences[b] 
    for e in c :
        for f in d :
            if e == f : 
                word.append(e)
                a1 = c.index(e) 
                a2 = c.index(f)
            if e != f : 
                    g = 0 
                    while g < len(e):
                        for h in range((g + 1) , (len(e) + 1)):
                            i = e[g : h]
                            if i == f :
                                word.append(f)
                        g += 1
    b += 1 

counts = []
for j in word :
    k = word.count(j)
    counts.append(k)
l = counts.index(max(counts))
m = word[l] 
n = 0
dict1 = {} 
while n < len(sentences) :
    o = sentences[n] 
    q = o.index(m)
    dict1.update({q : n}) 
    n += 1 
    r = max(dict1)
s = 0 
while s < len(sentences) :
    if s != dict1[r] :
        while str(sentences[s]).index(m) <= dict1[r] :
            sentences[s].insert(0 , '#')
    s += 1 
    if s == dict1[r] :
        s += 1 
for x in sentences :
    y = ' ' .join(x)
    print(y)