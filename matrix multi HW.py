#Matrix Multiplication

import random
x=[]
y=[]
z=[]
n=int(input('enter the size of your square arrays'))
for i in range (n):
    x.append(n*[0])
    y.append(n*[0])
    z.append(n*[0])
limit=0
limit=n*n
for i in range (n):
    for j in range(n):
        x[i][j]=random.randint(1,limit)
        y[i][j]=random.randint(1,limit)
print ('Array A=', x)
print ('Array B=', y)


for i in range(n):
    for j in range(n):
        for k in range(n):
            z[i][j]=z[i][j]+(x[i][k]+y[k][j])
print ('the multiplication of A and B gives us C=)', z)

