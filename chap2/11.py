with open('hightemp.txt', 'r') as f:
    l = f.read()
    print(l.replace('\t', ' '))
# cat hightemp.txt | sed 's/\t/ /g'
