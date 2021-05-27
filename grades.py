c=900000000
for i in range(1,c):
    a=input('Enter student name')
    if a=='done':
        break
    b=int(input('Enter Midterm score'))
    c=int(input('Enter final score'))
    avg=((b+c)/2)
    b=str(b)
    c=str(c)
    print('')
    print('Name:', a, 'Midterm:', b,'final:', c,'avergae:', avg)
    print('')
