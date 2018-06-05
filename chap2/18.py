with open('hightemp.txt', 'r') as f:
    t = sorted(f, key = lambda w: w.split()[2])

for i in t:
    print(i, end="")

#sort -k3 hightemp.txt
