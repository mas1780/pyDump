#The Leap Year program

#I have used the variable x since it was specified in the assignment
x = int(input('Please enter a year from 0 to 2500'))

#the correct input confirmation
if x>2500 or x<0:
    print ('Out of Range')
else:
    #here is the chunk of the program which determines the leap year
    if x%4==0:
        #making sure that it is divisbleby 4
        if x%400==0:
            #making sure it is divisible by 400
            print (x, 'is a leap year!')
        else:
            #this takes into consideration the years which are divisible by 4 but not by 400
            y=x%400
            if y%4==0:
                if y%100 != 0:
                    print (x, 'is a leap year')
                else: 
                    print (x, 'is not a leap year')
            else:
                 print (x, 'is not a leap year')
    if x%4!=0:
        #this outputs the message if x is not divisble by 4 in the first place
        print (x, 'is not a leap year')

    
