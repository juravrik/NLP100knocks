def ngram(s, n):
    gram=[]
    for i in range(len(s)-n+1):
        gram.append(s[i:i+n])
    return gram

X = set(ngram('paraparaparadise', 2))
Y = set(ngram('paragraph', 2))
print(X | Y)
print(X & Y)
print(X - Y)
print('se' in X)
print('se' in Y)
