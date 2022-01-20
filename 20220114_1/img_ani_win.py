from matplotlib import pyplot as plt
from matplotlib import animation
from time import sleep,time
from numpy import ndarray

INTERVAL=8 
# 动画速率，None为自动设置。
# 考虑到电脑配置，建议在原数据上减7左右

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
if INTERVAL is None:
    INTERVAL=sum(t)/len(t)
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
last=0

def up(frame):
    global last
    if frame%100==0:
        t2=time()
        print(frame,(t2-last)/100)
        last=t2
    f.set_data(x[:frame],y[:frame])
    # f=plt.scatter(x[frame],y[frame],color="black")
    # dt=t[i]-t[i-1]
    # sleep(1)
    return f,
ani=animation.FuncAnimation(fig,up,range(0,len(t),3),interval=INTERVAL,blit=True,repeat=False)
# f.show()
# fig.show(block=True)
# ani.save("img.mp4")
plt.show()

# plt.pause(0)