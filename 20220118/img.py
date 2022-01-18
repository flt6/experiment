from matplotlib import pyplot as plt
from numpy import  array
x=[]
y=[]
with open("out.txt","r") as f:
    for i in f:
        t1,t2=i.split(" ")
        x.append(float(t1))
        y.append(float(t2))
plt.title("X-Y")
len=max(max(x)-min(x),max(y)-min(y))+4
plt.xlim((min(x)-2,min(x)+len))
plt.ylim((min(y)-2,min(y)+len))
plt.plot(x, y,'.')
plt.grid()
plt.savefig("img.png",dpi=2000)
# plt.show(block=True)

