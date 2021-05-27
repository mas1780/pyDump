#random Array Matrix
import random
limit=0
x=[]
n=int(input('enter number'))
m=int(input('enter number'))
for i in range (n):
    x.append(m*[0])
print(x)
limit=n*m
for i in range (n):
    for j in range(m):
        
        x[i][j]=random.randint(1,limit)
print (x)
S=set()
for i in range (n):
    for j in range(m):
        z=random.randint(1,limit)
        while z in S:
            z=random.randint(1,limit)
        S.add(z)
        x[i][j]=z
print(x)
