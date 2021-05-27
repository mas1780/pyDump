x=0
binarySTR=''
remainder=0
remainderS= ''
LenComparison = 0
x = eval(input('enter number to be converted to binary'))
while x!=1:
    remainder= x%2
    remainderS= str(remainder)
    binarySTR= remainderS + binarySTR
    x= int(x/2)

binarySTR = '1'+ binarySTR
LenComparison= int(binarySTR)
if LenComparison<10000000:
    while len(binarySTR)<8:
        binarySTR= '0' + binarySTR


print ('The binary equivalent is ', binarySTR)

    
