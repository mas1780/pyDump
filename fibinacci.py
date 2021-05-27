m=[]
def fib(n):
    m=101*[0]
    m[0]=0
    m[1]=m[2]=1


def fib(n):
    if n<1 or n>100:
        print(n, "is out of range")
        return
    if m[n]!=0:
        return m[n]
    m[n]=fib(n-1)+fib(n-2)
    return m[n]

for i in range(1,101):
    print(i,fib(i))
