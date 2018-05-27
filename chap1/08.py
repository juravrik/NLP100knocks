def cipher(s):
    word=""
    for c in s:
        if c.islower():
            word+=chr(219-ord(c))
        else:
            word+=c
    return word

secret=cipher('encrypt')
print(secret)
print(cipher(secret))

