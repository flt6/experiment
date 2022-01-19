from matplotlib import pyplot as plt
from matplotlib import animation
from time import sleep
from numpy import ndarray
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
t.pop()
# To avoid Error because of Bug in main.cpp#23
fig=plt.figure(figsize=(5,5))
plt.title("X-Y")
len1=max(max(x)-min(x),max(y)-min(y))+0.1
plt.xlim((min(x)-0.05,min(x)+len1))
plt.ylim((min(y)-0.05,min(y)+len1))
plt.grid()

t[0]=0.001
plt.plot(x[0],y[0],'.')
f,=plt.plot(x[0],y[0],'.',color="red")
print(f)
def up(frame):
    # print(frame)
    f.set_data(x[:frame],y[:frame])
    # dt=t[i]-t[i-1]
    # sleep(1)
    return f,
ani=animation.FuncAnimation(fig,up,range(0,len(t)),interval=0.0001)
# f.show()
# fig.show(block=True)
plt.show()
# plt.pause(0)
