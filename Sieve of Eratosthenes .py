x=[]
primes=[]
for i in range(2,100):
    x.append(i)
while (len(x)!=0):
    k = x.pop(0)
    primes.append(k)
    k=int(k)
    T=100/k+1
    T=int(T)
    for j in range(2,T):
        m = j*k
        if m in x :
            x.remove(m)
print (primes)
