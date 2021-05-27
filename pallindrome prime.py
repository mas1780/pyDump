
def palindrome(s):
     if len(s) <= 1:
       return True
     else:
       if s[0] != s[len(s)-1]:
           return False
       else:
           return palindrome(s[1:len(s)-1])

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

count = 0
for i in range(2, 1000):
    if prime(i) and palindrome(str(i)):
        print (i),
        count += 1
        if count%5 == 0:
            print ('')
