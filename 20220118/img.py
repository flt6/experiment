from matplotlib import pyplot as plt
from numpy import array
x=[]
y=[]
t=[]
with open("out.txt","r") as f:
    for i in f:
        t1,t2=i.split(" ")
        x.append(float(t1))
        y.append(float(t2))
with open("FAccelerometer.csv") as f:
    f.readline()
    for i in f:
        t1,_,_,_=i.split()
        t.append(float(t1))
plt.figure(figsize=(5,5))
plt.title("X-Y")
len1=max(max(x)-min(x),max(y)-min(y))+0.1
plt.xlim((min(x)-0.05,min(x)+len1))
plt.ylim((min(y)-0.05,min(y)+len1))
plt.grid()

# plt.savefig("img.png",dpi=2000)


t[0]=0.001
for i in range(len(t)):
    dt=t[i]-t[i-1]
    if dt<=0:dt=0.001
    # print(dt)
    plt.plot(x[i], y[i],'.',color="black")
    plt.pause(dt)


# plt.show(block=True)
plt.pause(0)
