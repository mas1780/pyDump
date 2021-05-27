#this is my first file
print('Hello World')
print('I am amazed')
message = "Hey there wolrd!"

#assigns the variable a string value 
print message
print (len(message))

#prints the length of the string. OT = 16
print (message[1])

#prints the index position of the string according to value in block. OT=e
print (message[0:3])

#prints the part as defined by the index and leght. OT = Hey
print (message.lower())

#prints all in lowercase 
print (message.upper())

print (message.count('e'))
#prints the number of the argument, which is e in this case. OT = 3

#to find a certain item in the string use the find function. ot = 4
print (message.find("there")) 

name = "Gamer"
greet = "Welcome! Sir"
boy = "Cheetay!"

message = name + " " + greet
print message
#basic concatination 

message = "{}, {} {}".format(greet, name, boy)
#this helps concatinate mutliple strings together. 

print message

#print (help(str))
#a catalogue of all the possible things you can do with the str data

#now you will make your first program which will input something from the user.

s1 = float(input("enter 3 numbers"))
s2 = float(input())
s3 = float(input())

sum = s1 + s2 +s3
avg = sum/3

print (avg)
           






