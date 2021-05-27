
'''
#Lab
#Q1
 1.Ture
 2.'Hello'
 3.False
 4.True
 5.True
 6.'Hello'
 7.'HelloHelloHelloHelloHello'
 8.'Hello\nHello\nHello\nHello\nHello\n'
 9.hello
   hello
   hello
   hello
   hello
 10.hello
   hello
   hello
   hello
   hello

'''
'''
#Q2

hours = eval(input('How many hours did you work?'))
WageRate = eval(input('What is the wage rate?'))
ExtraHours = 0
ExtraHours = hours - 40
X = ExtraHours > 0 
hours = hours - (ExtraHours*X) 
StraightPay = hours*WageRate
OverTimePay = ExtraHours * (WageRate*1.5)*X
TotalPay = StraightPay + OverTimePay
print ("total salary")
'''
'''
a=1
while True:
    a+=1
    print('#'*a)

    if a%5==0:
        break

'''


print ("Number", end= "\t")
print ()
counter = 0
while counter < 10:
    print (format(counter, "<5d"), format(counter*2, "<5d"))
    counter += 1
    
