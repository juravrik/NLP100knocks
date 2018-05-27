def ngram(s, n):
    gram=[]
    for i in range(len(s)-n+1):
        gram.append(s[i:i+n])
    return gram

s = "I am an NLPer"
print(ngram(s.split(' '), 2))
print(ngram(s, 2))
