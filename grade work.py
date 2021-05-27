x=[]
a='A'
b=0
c=0
AV=0
average=[]
y=[]
z=[]
CLSavg=0
CLSsum=0
c=900000000
deviation=[]
dev=0
ANA=0
for i in range(1,c):
    a=input('Enter student name')
    if a=='done':
        break
    x.append(a)
    b=int(input('Enter Midterm score'))
    c=int(input('Enter final score'))
    
    AV=((b+c)/2)
    
    CLSsum=CLSsum+AV
    CLSavg=CLSsum/i

    dev=AV-CLSavg
    b=str(b)
    c=str(c)
    AV=str(AV)
    dev=str(dev)
    deviation.append(dev)
    y.append(b)
    z.append(c)
    average.append(AV)
    
    ANA=ANA+1
COMBINE='string'    
CLASS=[]
print ('name', end='    ')
print ('Midterm', end='    ')
print ('Final', end='    ')
print ('Average', end='    ')
print ('Deviation', end='    ')
print('')
for c in range(0,ANA):
    COMBINE=(x[c]+'       '+y[c]+'        '+z[c]+'          '+average[c]+'           '+deviation[c])
    print (COMBINE)


    
    
    
