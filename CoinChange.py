#coin Change Homework


Money = eval(input('enter money so I calculate change'))

halfDollar = 0.5
quarters = 0.25
dimes = 0.1
nickels = 0.05
penny = 0.01

Half_Dollar=Money//0.5
Money = Money - Half_Dollar*halfDollar
Quarter =Money//0.25
Money = Money - Quarter*quarters
Dime =Money//0.1
Money= Money- Dime*dimes
Nickel = Money//0.05
Money = Money - Nickel*nickels
Penny= Money

print ("Half dollars=", Half_Dollar)
print ('Quarters=', Quarter)
print ('Dimes =', Dime)
print ('Nickels =', Nickel)
print ('Penny=', format(Penny,'.2f'))


