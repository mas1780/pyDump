def findPrimes(n):
    A = []
    B = []
    for i in range(2, n+1):
        if i not in A:
            B.append(i)
            for j in range(i*i, n+1, i):
                A.append(j)
    return B

inp = 100
print(findPrimes(inp))
