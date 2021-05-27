import random
x=input('Enter number')
t=[]
d=0
smallestindex=0
if x!='done':
    x=int(x)
    WT=x*3
    for count in range (0,WT):
        d = random.randint(1,9)
        t.append(d)
    for E in range (0,WT):
        smallestindex=E
        for Q in range(E+1,WT):
            if t[Q]<t[smallestindex]:
                smallestindex=Q
        temp=t[E]
        t[E]=t[smallestindex]
        t[smallestindex]=temp
        
print(t)
    
