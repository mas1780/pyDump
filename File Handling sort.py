def last_then_first(x):
    return x[1]+x[0]

file=open('scores.txt')
av=0
cav = 0
grades=[]
for line in open('scores.txt'):  
    line=line.split()
    line[2]=float(line[2])
    line[3]=float(line[3])
    grades.append(line)
    cav+=(line[2]+line[3])/2
cav=cav/len(grades)

outfile=open('results.txt','w')
grades.sort(key=last_then_first) 
for line in grades:
    av=(line[2]+line[3])/2 
    line=format(line[0],'<10s')+format(line[1],'<10s')+str(line[2])+'  '+str(line[3])+'  '+str(av)+'  '+str(av-cav)+'\n'
    outfile.write(line)
outfile.close()
print('Name','\t','Midterm','\t','Final','\t','Average','\t','Deviation')
print()
file=open('results.txt','r')
Output = file.read()
print(Output)
print()
print('Class Average is:',cav)
