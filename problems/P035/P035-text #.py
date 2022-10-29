sentences = []
word = []
words = []
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
                words.append(f)
                if b == 1 :
                    words.append(e)
            if e != f : 
                g = 0 
                while g < len(e):
                    for h in range((g + 1) , (len(e) + 1)):
                        i = e[g : h]
                        if i == f :
                            word.append(f)
                            words.append(e)
                            if b == 1 :
                                words.append(e)
                    g += 1
            if e != f : 
                g = 0 
                while g < len(f):
                    for h in range((g + 1) , (len(f) + 1)):
                        i = f[g : h]
                        if i == e :
                            word.append(e)
                            words.append(f)
                            if b == 1 :
                                words.append(e)
                    g += 1
    b += 1 

lentghs = list(map(lambda x : len(x) , word))
lentgh = set(word)
l = lentghs.index(max(lentghs))
m = word[l]
trashes_words = [] 
for le in lentgh :
    if le != m : 
           trashes_words.append(le)
for gh in words :
    if gh in trashes_words :
        hg = words.count(gh) 
        for gh1 in range(hg):
            words.remove(gh)
index = [] 
wo = 0 
while wo < len(sentences) :
    the_word = words[wo] 
    the_sentence = sentences[wo] 
    jo = ' '.join(the_sentence)
    index.append(jo.index(the_word))
    wo += 1 
max_index = max(index) 
the_index = index.index(max_index)
ow = 0 
while ow < len(sentences) :
    tword = words[ow] 
    tsentence = sentences[ow]
    tsentence1 = ' ' .join(tsentence)
    if tsentence1.index(tword) != max_index :
        abcd = max_index - tsentence1.index(tword) - 1
        tsentence.insert(0 , '#' * abcd)
        string_sentence = ' '.join(tsentence)
        print(string_sentence)
    if tsentence1.index(tword) == max_index :
        string_sentence = ' '.join(tsentence)
        print(string_sentence)
    ow += 1 