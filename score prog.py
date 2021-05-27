Team=0
while Team==0:
    String= input('ENTER IN CAPITALS THE ORDER OF THE RACE RESULTS')
    Team=String.count('A')
    if Team==0:
        Team=String.count('B')
        if Team==0:
            Team=String.count('C')
            if Team==0:
                Team=String.count('D')
                if Team==0:
                    Team=String.count('E')
                    if Team==0:
                        Team=String.count('F')
                        if Team==0:
                            Team=String.count('G')
                            if Team==0:
                                Team=String.count('H')
                                if Team==0:
                                    Team=String.count('I')
                                    if Team==0:
                                        Team=String.count('J')
                                        if Team==0:
                                            Team=String.count('K')
                                            if Team==0:
                                                Team=String.count('L')
                                                if Team==0:
                                                    Team=String.count('M')
                                                    if Team==0:
                                                        Team=String.count('N')
                                                        if Team==0:
                                                            Team=String.count('O')
                                                            if Team==0:
                                                                Team=String.count('P')
                                                                if Team==0:
                                                                    Team=String.count('Q')
                                                                    if Team==0:
                                                                        Team=String.count('R')
                                                                        if Team==0:
                                                                            Team=String.count('S')
                                                                            if Team==0:
                                                                                Team=String.count('T')
                                                                                if Team==0:
                                                                                    Team=String.count('U')
                                                                                    if Team==0:
                                                                                        Team=String.count('V')
                                                                                        if Team==0:
                                                                                            Team=String.count('W')
                                                                                            if Team==0:
                                                                                                Team=String.count('X')
                                                                                                if Team==0:
                                                                                                    Team=String.count('Y')
                                                                                                    if Team==0:
                                                                                                        Team=String.count('Z')
                                                                                                        if Team==0:
                                                                                                            print ('You Made a mistake. Capitals Please')
                                                                                                            continue 
        
L=[]                           #create an empty list
for letter in String:
    if letter not in L:
        L.append(letter)       #append unique chars to list

print ('Number of teams=', len(L))
print ('Number of Runners Per Team=', Team)


if Team>0:
    AA=0
    scoreA=0
    for i in range (Team):
        AA= String.index('A',AA)
        AA=AA+1
        scoreA+=AA
print (scoreA)
