#The Multiplication Table 


n=int(input('enter your number'))
n=n+1
for i in range(1,n):
    for k in range(1,n):
        print (i*k, end="\t")
    print("")
