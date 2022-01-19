from cProfile import label
from matplotlib import pyplot as plt
f=open("FAccelerometer.csv","r")
f.readline()

t=[]
ax=[]
ay=[]
for i in f:
    a,x,y,_=i.split()
    t.append(float(a))
    ax.append(float(x))
    ay.append(float(y))

f,(x,a,b)=plt.subplots(3,1,sharey=True,sharex=True)

plt.xlabel("Time(s)")
plt.ylabel("Accelerometer(m/s^2)")
x.plot(t,ax,label="X")
x.plot(t,ay,label="Y")

a.plot(t,ax,'.',label="X")
b.plot(t,ay,'.',label="Y")

a.legend()
a.grid()
b.legend()
b.grid()
x.legend()
x.grid()


# plt.show(block=True)
plt.savefig("data.png",dpi=800)