
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
Tax = MonthlyPay*(0.28)
MonthlyPay = MonthlyPay - Tax
YearPay = MonthlyPay*12
Party= (MonthlyPay*(0.4/8))
Vacation = (MonthlyPay*(0.2*2))
MonthlyExpenses = MonthlyPay*0.4
print ('Straight Pay=', StraightPay, 'Dollars')
print ('OverTime Pay=', OverTimePay, 'Dollars')
print ('Total Pay =', TotalPay, 'Dollars')
print ('Monthly', MonthlyPay,' And for our monthly party, aka on one weekend day you can spend,', Party)
print ('For Monthly Expense we have', MonthlyExpenses, 'dollars')
print ('For our Vacations every two months we have', Vacation,'dollars')
print ('And This is the Yearly pay after tax', YearPay)
print ('lets say you dont go for holidays every two months and you save that money')
YearSavings = Vacation*6
print ('we save ', YearSavings , ' in savings per year')
print("lets say we start saving and investing with a beginning total of 100000 and add our saving each year to the investments")
Sum = 0
Principal =  200000
InterestRate = eval(input('enter average yield rate = '))
Years = eval(input('how many years do you keep compoudning? = '))
for i in range (1, Years+1):
    Sum = Principal*(1+(InterestRate/100))
    Principal = Sum
    Principal += YearSavings
    print('After ',i, ' years, you will have compounded a total of ', Principal)
ActualGain = Principal - (Years*YearSavings)
print('through interest we gain ', ActualGain, ' in those years. ')
YearGain = ActualGain/Years
print ('On average, in those years, we will make the following amount just by interest each year =', YearGain)


    

       


