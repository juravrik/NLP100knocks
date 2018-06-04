with open('hightemp.txt', 'r') as f:
    l=f.readlines()

with open('col1.txt', 'w') as f: 
    f.writelines('\n'.join(list(map(lambda x:x[0], l))))

#cut -b 1-3 hightemp.txt

with open('hightemp.txt', 'r') as f:
    l=f.readlines()

with open('col2.txt', 'w') as f: 
    f.writelines('\n'.join(list(map(lambda x:x[1], l))))

#cut -b 4-6 hightemp.txt
