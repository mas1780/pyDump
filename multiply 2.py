n=int(input('Please enter the size:'))
print(5*' ',end="")
for i in range(1,n+1):
    print(format(i,'^6d'),end='')
print("")
print(5*' '+'-'*6*n)
#Here I will add the normal multiplication table code from last assignment
for a in range(1,n+1):
    print(a,'* ',end=' ')
    for j in range(1, n+1):
        print(format(a*j,'^6d'), end='')
    print("")
