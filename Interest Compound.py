'Calculating my savings compounded each year'

Sum = 0
Principal =  eval(input('enter principal = '))
InterestRate = eval(input('enter each year interest rate = '))
Years = eval(input('how many years do you keep compoudning? = '))
for i in range (0, Years):
    Sum = Principal*(1+(InterestRate/100))
    Principal = Sum
    print('After ',i, ' years, you will have compounded a total of ', Principal)

    
