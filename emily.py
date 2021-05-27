import random
# Create 3X3 matricies 
a=[3*[0] for i in range(3)]
b=[3*[0] for i in range(3)]
c=[3*[0] for i in range(3)]

print (a)

# Now fill the entries with random integers
for i in range(3):
    for j in range(3):
        a[i][j]=random.randint(0,3)
        b[i][j]=random.randint(0,3)
print (a)

def get_row(x,i):
    return x[i]

def get_column(x,i):
    return [x[k][i] for k in range(len(x))]

def diagonalsum(x):
    n=0
    for i in range (len(x)):
        n=n+x[i][i]
    return (n)
    
    
row=int(input('which row you want?'))
w=get_row(a,row)

column=int(input('which column you want?'))
c=get_column(a,column)

DSUM= diagonalsum(a)
print ('diagonal sum =', DSUM)

print (w)
print (c)
        
