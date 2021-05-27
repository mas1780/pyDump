import random
A=[]
B=[]
C=[]

m=int(input('enter array width'))
n=int(input('enter array height'))
from random import randint
n = int(input("Please enter an integer: "))
m = int(input("Please enter another integer that is larger than the previously entered integer: "))

x = []
while len(x) < n:
  for i in range(n):
    y = randint(1, m)
    if y not in x:
      x.append(y)
print(x)
for i in range (n):
    A.append(m*[0])
print (A)
for i in range (n):
    B.append(m*[0])
print (B)

limit=n*m

for i in range(m):
    for j in range(n):
        A[j][i]=random.randint(1,limit)
        B[j][i]=random.randint(1,limit)

print(A)
print(B)

for i in range (m):
    for j in range (n):
        C[j][i]=C[j][i]+(A[j][i]*B[j][i])
print (C)
        


        
