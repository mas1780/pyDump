#The Arrow assignment 

stars=0
x=0
x=input('how many columns?')
while x!='done':
    x=int(x)
    while stars<x:
        print (' '*stars,'*')
        stars=stars+1
    stars=stars-1
    while stars>0:
        stars=stars-1
        print (' '*stars,'*')
    x=input('how many columns?')
print ('bye')        
