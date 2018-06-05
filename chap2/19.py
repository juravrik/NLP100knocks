with open('hightemp.txt', 'r') as f:
    d = dict()
    for w in f:
        try:
            d[w.split()[0]]+=1
        except KeyError as e:
            d[w.split()[0]]=1

print(sorted(d, key=lambda x:d[x], reverse=True))

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r

