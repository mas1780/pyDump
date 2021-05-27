def lastandfirst(x):
    return x[1]+x[2]
    


file=open('scores.txt')
total = 0
average = []
for i in f:
    Place=i.split()
    AVG=(int(Place[2])+int(Place[3]))/2
    average.append(AVG)
    total=total+AVG
CAverage = float(total/(len(average)))
Variation = []
for i in range(len(average)):
    d = average[i] - CAverage
    Variation.append(d)
f.close() 

f=open('scores.txt')
j=0    
List=[]
for i in f:
    s=i.split() 
    s='\t'.join(s)
    line=s + '\t'  + str(average[j]) + '\t' + str(deviation[j])+'\n'
    List.append(line)
    j+=1

List=Lists.sort

outfile=open('results.txt','w')
outfile.writelines(List)
outfile.close()
print('Name','\t','Midterm','\t','Final','\t','Average','\t','Deviation')
print()
file=open('results.txt','r')
Output = file.read()
print(Output)
print()
print('Class Average is:',CAverage)
