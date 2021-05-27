def SORTteams(x):
    z=sorted(set(x))
    return z

def validation(race):
    t=SORTteams(race)
    num=race.count(t[0])
    for i in t:
        if race.count(i)!=num:
            return False
    return True

def score(a,x):
    s=0
    c=x.count(a)
    for i in range(len(x)):
        if x[i]==a:
            s+=i+1
    return s/c
XYZ=0
Winning_team=XYZ
race=0
while race!="end" or Winning_team==XYZ:
    race=input("Enter the race results IN CAPTIALS: ")
    if not validation(race):
        print("Incorrect results!")
        race=input("Enter the race results IN CAPITALS: ")
        continue
    t=SORTteams(race)
    L=[]                         
    for letter in race:
        if letter not in L:
            L.append(letter)
    first=t[0]
    Team_Size=0
    Team_Size=race.count(first)
        
    print('Number of teams=', len(L))
    print('The Number of Runners per team=', Team_Size)
    print("The teams are",t)     
    print("The teams with scores:")
    winning_score=score(t[0],race)
    Winning_team=t[0]
    for i in t:
        if winning_score>score(i,race):
            winning_score=score(i,race)
            Winning_team=i
        print(i,score(i,race))
    print()
    print("The winning team is team",Winning_team, "with score",winning_score)
    continue 
