s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.split()
key=[]
for index, word in enumerate(s):
    if index+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        key.append(word[0])
    else:
        key.append(word[:2])
dic = dict(zip(key, s))
print(dic)
