t2=[]
with open('Gyroscope.csv','r') as f:
    t=f.readlines()
    for i in t:
        t2.append(i.split(','))
with open("FGyroscope.csv","w") as f:
    for i in t2:
        print(' '.join(i),file=f,end='')