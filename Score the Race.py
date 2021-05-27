def valid(x):
    G=0
    Alphabet=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    for i in range (25):
        G+=x.count(Alphabet[i])
    TeamS=x.count('A')
    DivideCheck=G/TeamS
    if DivideCheck//1==0:
        return valid
    else:
        return false




String= input('ENTER IN CAPITALS THE ORDER OF THE RACE RESULTS')
while String!="done":
    if not valid(String):
        print("oops! Invalid results!")
        race=input("Please enter the race results: ")
        continue

Team=String.count('A')
L=[]                           #create an empty list
for letter in String:
    if letter not in L:
        L.append(letter)       #append unique chars to list

print ('Number of teams=', len(L))
print ('Number of Runners Per Team=', Team)


