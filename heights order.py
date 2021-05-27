#Height Order
import random 
kids=[900,919,901,918,902,917,903,916,904,915,910,905,914,906,913,907,912,908,911,909]
limit=len(kids)
limit-limit-1
first=0
S=set()
ad=[]
recount=0
count=0
store=0
first=random.randint(0,19)
while sorted!=1:
    if kids[first]>kids[count]:
        store=kids[first]
        kids[first]=kids[count]
        kids[count]=store
        store=0
    if kids[first]<kids[count]:
        count=count+1
    if count==19:
        ad.append(kids[first])
        S.add(kids[first])
        first=random.randint(0,19)
        while first in S:
            first=random.randint(0,19)
        count=0

print (ad)
        
        
