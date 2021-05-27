
#SALARY HOMEWORK 


#Without the if statement 
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

#With the if statement
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
