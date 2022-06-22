import random

#set-up your elements weight 
probs = [0.25,0.21,0.12,0.08,0.34]

n = len(probs)
a = [-1]*n
p = [0]*n
fixed = 0
last = -1
timelast = 0

while fixed < n:
    if timelast > 3:
        p[last] = probs[last]
        break

    #block assignment of small items
    for i in range(n):
        if p[i] == 0 and probs[i] <= 1/n :
            p[i] = probs[i] 
            probs[i] = 0
            fixed += 1

    # packing of large items
    for i in range(n):
        if probs[i] > 1/n:
            if last == i:
                timelast +=1
            else:
                last = i
                timelast = 0
            
            for j in range(n):
                if p[j] != 0 and a[j] == -1:
                    a[j] = i
                    probs[i] -= (1/n - p[j])
                if probs[i] <= 1/n:
                    break     



print('lstProbs:',p)
print('alias:',a)
ttalias = 0
ttnoalias = 0
counts = [0] * n



for _ in range(1000000):
    i = int(random.random()*n) # get id in the lst
    q2 = random.random()*1/n   # get weight for alias

    #alias or no ?
    if q2 < p[i]:
        counts[i] += 1
        ttnoalias+=1
    else:
        counts[a[i]] += 1
        ttalias +=1


print("count: ",counts) # -> [20014, 30023, 40081, 9882] (for example)


#print % for each elements
total = 0
for i in range(len(counts)):
    print("->",counts[i]/10000)
    total = total +  counts[i]/10000
print(total)

