import sys

with open('hightemp.txt', 'r') as f:
    l = f.readlines()
    n = int(sys.argv[1])
    for i, seg in enumerate(zip(*[iter(l)]*int(len(l)/n))):
        with open('segment'+str(i)+'.txt', 'w') as w:
            w.write(''.join(seg))

# split -l 分割後の行数 hightemp.txt
