import sys

with open('hightemp.txt', 'r') as f:
    l = f.readlines()
    for i in l[:int(sys.argv[1])]:
        print(i.rstrip())

# head -任意の数字 hightemp.txt
