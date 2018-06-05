with open('hightemp.txt', 'r') as f:
    s=set()
    for l in f:
        s.add(l.split()[0])

for i in s:
    print(i)

#cut -f 1 hightemp.txt | uniq
