'''
# a is the right-most digit, b is second from right
def get_nums(n):
    a=n%10
    b=(n//10)%10
    return a,b

i=1
while True:
    a,b=get_nums(i*i)
    if a%2 == 1 and b%2 ==1: # if the two right-most digit are odd, print the value
        break 
    i+=1
print(i*i)
'''
'''
n=int(input('Please enter the size of the table: '))
print(5*' ',end='')
for i in range(1,n+1):
    print(format(i,'^6d'),end='')
print()
print(5*' '+'-'*6*n)
for i in range(1,n+1):
    print(i,'* ',end=' ')
    for j in range(1, n+1):
        print(format(i*j,'^6d'), end='')
    print()
'''

cards=[919,918,917,916,915,914,913,912,911,910,909,908,907,906,905,904,903,902,901,900]
print(cards)
length=len(cards)
j=0
for i in range(1,length):
    j=i
    while j>0 and cards[j]<cards[j-1]:
        cards[j],cards[j-1]=csards[j-1],cards[j]
        j=j-1
print (cards)


cards=[919,918,917,916,915,914,913,912,911,910,909,908,907,906,905,904,903,902,901,900]
print(cards)
count=0
# Next five lines is the sort
for i in range(1,len(cards)):
    j=i
    while j>0 and cards[j]<cards[j-1]:
        cards[j],cards[j-1]= cards[j-1], cards[j]
        count+=1
        j-=1
print(cards)
print(count)
