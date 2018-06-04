with open('col1.txt', 'r') as f1, open('col2.txt', 'r') as f2:
    l1, l2 = f1.readlines(), f2.readlines()

with open('merge.txt', 'w') as f:
    f.write('\n'.join(
        ['\t'.join([c1.rstrip(), c2.rstrip()]) 
        for c1, c2 in zip(l1, l2)]))

#paste col1.txt col2.txt
