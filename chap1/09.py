import random
def randamize(s):
    r = s.split()
    ans=[]
    for w in r:
        if len(w)<=4:
            ans.append(w)
            continue
        print(w)
        mid = list(w[1:-1])
        random.shuffle(mid)
        mid = ''.join(mid)
        ans.append(w[0]+mid+w[-1])

    return ' '.join(ans) 

sample="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(randamize(sample))
