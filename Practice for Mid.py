#Practice Midterm

'''
W=0
while W<3:

    x=int(input('Please enter your password'))

    if x>99 or x<10:
        print('Invalid Password please try again')
        W=W+1
        break
    else:
        n1=x%10
        n2=x//10
        if n1%2==0 and n2%2==0:
            print ('Correct! You may access the system')
            W=4
        else:
            print('Invalid Password please try again')
            W=W+1
    if W==3:
        print('Too many invalid attempts. Please try again')
'''

'''
largest=-99999

while x!='done':
    for i in range (1,900000):
        x=input('enter number')
        if x=='done':
            break
        n=int(x)
        if n>largest:
            largest=n
            position=i
print('largest number is',n,' on the position',position)
        
    
'''


'''
k=1
m=int(input('enter m'))
n=int(input('enter n'))
d=m/n
d=d+1
s=int(d)
for j in range (1,s+1):
    for l in range (1,n+1):
        if k>m:
            break
        print(k, end=' ')
        k=k+1
        
    print('')
    
'''

'''

S=0
x=0
j=0
while x!='done':
    x=input('enter number')
    if x=='done':
        break
    n=int(x)
    S=S+n
    j=j+1
print (S)
print (S/j)
        
'''

'''
SUM=0
L=input('enter number')
K=int(L)
for i in range (1,K):
    if i%2==1:
        SUM=SUM+i
    if i%2==0:
        SUM=SUM-i
print (SUM)


'''
'''
for n in range(2, 1001):
  temp=n
  rev=0
  while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
  if(temp==rev):
    prime=True
    for i in range (2,temp):
        if temp%i==0:
            prime=False
            break
    if prime:
        print(temp)
'''
Limiter=0
n1=input('enter number1')
n2=input('enter number2')
if n1>n2:
    Limiter=n2
else:
    Limiter=n1
    for r in range (1,Limiter):
        n1

    










    
