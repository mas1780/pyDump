import random
A=[[]]
B=[[]]
null=0
number=int(input('enter number'))
for i in range(number):
    for j in range(number):
        A[i][j].append(null)
for i in range(number):
    for j in range(number):
        randI=random.randint(1,9)

        A[i][j]=randI
print (A)





'''
for i in range (3):
    for j in range(3):
        s=0
        for k in range(3):
            s=s+a[i][k]*b[k][j]
        c[i][j]=s
