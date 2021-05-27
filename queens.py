#8QUEENS
def duplicates(q):
    if len(q)!=len(set(q)):
        return True
    else:
        return False
def diagonal_threat(q):
    for col in range (7,0,-1):
        for i in range(col):
            T=abs(q[col]-q[i])
            if col-i==T:
                return True
    return False
count=0
for a in range(0,7):
    for b in range(0,7):
        for c in range(0,7):
            for d in range(0,7):
                for e in range(0,7):
                    for f in range(0,7):
                        for g in range(0,7):
                            for h in range(0,7):
                                

                                q=[a,b,c,d,e,f,g,h]
                                if duplicates(q) or diagonal_threat(q):
                                    continue
                                count+=1
                                print('solution ',count,': ',q) 
