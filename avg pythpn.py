'''

x = int(input('enter number'))
print (x)
print ('line 1', end='-*-*-')
print ('a','b','c')
print (1,2,3,4,5,6, sep="X")

'''

'''
name = input('what\'s your name?')
print ('thanks', name, '!')

'''

#get 4 words from the user
#store in 4 different variables
#use words in print statements
#print out a story for the user

'''
noun = input('enter noun please!')
verb =  input('enter a verb now...')
adjective = input('adjective.')
adverb = input('finally an adverb!')

#this is the story you want:
# the [adjective][noun] was very hungry, so it decided to [adverb][verb] to the nearest restaurant.

print ('The', adjective, noun, 'was very hungry, so it decided to', adverb, verb, 'to the nearest restaurant')
'''

'''
num1 = int( input('enter number')) 
num2 = float( input('second number'))
sum = num1 + num2
total = format(sum, .2f)
print (total)
'''


#the MOD funtion can be written with the percentage sign. gives remainder. OT=4
#print (9%5)

#MAKE SURE YOU STUDY ABOUT FLOATING POINT NUMBERS AND HOW TO GET RID OF THE EXTRA DECIMALS

#BOOLEAN :
#greater than equal to : >= or less than : <=
#equal to : ==
#not equal to !=

#Boolean operators
#and, or & not

'''
True and True
= True
 False and False
=Fasle
False or True
= True

True and 6
= 6
True or 6
= True
False and 6
= False (bcz the program has an option other than 6 now)
'''
'''
"3" == 3
= False
#this it about Data types not being the same 
"True" == True
= False
'''

'''
Inside the computer True represents the integer 1 and False represents 0
So (7>5)*6
OT = 6
and (7<5)*6
OT = 0
'''

'''
1 2 3 Example
>>> print (1,2,3)
1 2 3
>>> print (1,2,3, sep='#')
1#2#3
>>> print (1,2,3, sep='\n')
1
2
3
>>>
'''
'''
age = int(input("Enter age"))
seconds = age*365*24*60*60
print ("Your age in seconds is", seconds, "Seconds")
'''
'''
FTemp = eval(input("Enter the temperature in Feranhiet"))
CTemp = (FTemp - 32)*(5/9)
print ("Temperature in Celcius =", int(CTemp+0.5))
'''
'''
Number = int(input("Enter your number"))
T= (Number%2 == 0)
X= (Number%2 == 1)
Y= T*"Even" + X*"Odd"
print (Y)

'''
'''
hours = eval(input('How many hours did you work?'))
WageRate = eval(input('What is the wage rate?'))
ExtraHours = 0
if hours > 40:
    ExtraHours = hours - 40
    hours = 40 
StraightPay = WageRate * hours
OverTimePay = ExtraHours * (WageRate*1.5)
TotalPay = StraightPay + OverTimePay
print ('Straight Pay=', StraightPay, 'Dollars')
print ('OverTime Pay=', OverTimePay, 'Dollars')
print ('Total Pay =', TotalPay, 'Dollars')
'''
#print ('You should be paid,', Salary, 'dollars for working', hours,'hours at a rate of', WageRate, 'dollars per hour.')


#THE SALARY HOMEWORK
'''
hours = eval(input('How many hours did you work?'))
WageRate = eval(input('What is the wage rate?'))
ExtraHours = 0
ExtraHours = hours - 40
X = ExtraHours > 0 
hours = hours - (ExtraHours*X) 
StraightPay = hours*WageRate
OverTimePay = ExtraHours * (WageRate*1.5)*X
TotalPay = StraightPay + OverTimePay
print ('Straight Pay=', StraightPay, 'Dollars')
print ('OverTime Pay=', OverTimePay, 'Dollars')
print ('Total Pay =', TotalPay, 'Dollars')
'''             

'''
hours = eval(input('How many hours did you work?'))
WageRate = eval(input('What is the wage rate?'))
ExtraHours = 0
if hours > 40:
    ExtraHours = hours - 40
    hours = 40
StraightPay = WageRate * hours
OverTimePay = ExtraHours * (WageRate*1.5)
TotalPay = StraightPay + OverTimePay
MonthlyPay = TotalPay*4
YearPay = MonthlyPay*12
Tax = YearPay*(28/100)
Final = YearPay - Tax
Party= (MonthlyPay*(0.4/8)) 
print ('Straight Pay=', StraightPay, 'Dollars')
print ('OverTime Pay=', OverTimePay, 'Dollars')
print ('Total Pay =', TotalPay, 'Dollars')
print ('Monthly', MonthlyPay,'monthly party, aka on one weekend day you can spend,', Party)
print ('Yearly', YearPay)
print ('Final Pay=', Final)
'''             



#changing sequence 
'''
x = 5
y = 10
z = x
x = y
y = z


print (x,y)
'''



#the rolling of a dice
'''

import random
x = random.randint(1,6)
s = 'you rolled '
if x == 1:
    print (s+'a one!')
elif x==2:
    print (s+' a two!')
elif x==3:
    print (s+' a three!')
elif x==4:
    print (s+' a four!')
elif x==5:
    print (s+' a five!')
elif x==6:
    print (s+ ' a six!!')
else:
    print ('something is off it seems')

    
'''

'''
x1= eval(input('enter number 1'))
x2 = eval(input('enter number 2'))
x3= eval(input('enter number 3'))
x4 = eval(input('enter number 4'))
x5= eval(input('enter number 5'))
max=x1

if x2>max:
    max= x2
if x3>max:
    max= x3
if x4>max:
    max= x4
if x5>max:
    max= x5

print (max, 'is the maximum amount')

'''

'''
score = eval(input('Enter your score'))
grade = 'F'
if score >= 90:
    grade = 'A'
elif score>=80:
    grade = 'B'
elif score >=70:
    grade= 'C'
elif score>=60:
    grade = 'D'
else:
    grade = grade
print (grade)
'''

'''

#CHECKING PALLINDROME
n = eval(input('enter your number'))
d= n%10
n = n//10
c = n%10
n= n//10
b= n%10
n=n//10
a = n%10

if a == d and c == b:
    print ('Pallindrome!')
else:
    print ('not pallindrome...')
    
#TRY INPUTTING A NUMBER AND REARRANGING THE NUMBER BACKWARDS. USE THE SEP METHOD
'''

'''
#Program for negative count. WHILE LOOP
i=1
n=int(input('enter number where you want me to count'))
while i<=n:
    if n%2==0:
        print (n)
    n=n-1
'''

'''
stars=0
x=0
x=input('how many columns?')
while x!='done':
    x=int(x)
    while stars<x:
        print (' '*stars,'*')
        stars=stars+1
    while stars>0:
        stars=stars-2
        print (' '*stars,'*')
    x=input('how many columns?')
print ('bye')        
    

'''
'''
n=int(input('Enter your number for the factorial'))
PI=1
p=1
while PI<=n:
    p=p*PI
    PI=PI+1
print ('the factorial answer is:', p)
'''


'''
print ('welcome')
attempts=1
while attempts<=3:
    PASS=int(input('Enter your two digit even password'))
    if PASS%2==0:
        if PASS<100:
            print ('You got it right!')
            break 
    else:
        attempts=attempts+1
        if attempts>3:
            print('Loser!')
            break
        print ('Yo! Get your Shit straight! Try again!')
'''        

'''

for i in range (3):
    for j in range(4):
        print ("i",i, 'j',j)

'''
'''
n=int(input('enter your number'))
n=n+1
for i in range(1,n):
    for k in range(1,n):
        print (i*k, end="\t")
    print(end="\n")
'''


'''
#this prints the numbers separately as strings
n=int(input('enter number'))
while n>0:
    print(n%10)
    n=n//10
'''

'''
#this is to print the number the other way around but as an integer 
n=int(input('enter number'))
s=0
while n>0:
    s=s*10+n%10
    n=n//10
print (s)

'''
'''

prime=True
n=int(input('enter number'))
for i in range (2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print(n, 'is prime')
else:
    print(n, 'is composite')

'''

'''
n=int(input('enter number'))
for i in range (1,n):
    n=n+i
print(n)
'''       

'''
n=int(input('enter number'))
for i in range(1,n):
    n=n*i
print (n)

'''
'''
n=int(input('enter number'))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print(sum)
'''

'''
#this is the sum = 20 program which you didnt get correct
for n in range (1,1001):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
        if sum==20:
            print(n)
'''


#FIRST FUNTION CODE
'''
x=int(input('enter X'))
y=int(input('enter Y'))

def gt(x,y):
    if x>y:
        return True
    else:
        return False
print(gt(x,y))
'''

'''
for r in range (1,1):
    print('A')


'''

#LISTS
'''
from random import random,randint
position=0
Max=0
x=[]
for i in range (10):
    r=randint(1,10)
    if r>Max:
        Max=r
        position=i
    x.append(r)
print(x)
print(Max, 'at', position)
'''

#2 Dimensional Lists

a=[[1,2],[3,4]]
print (a)
leng= len(a)
print (leng)




