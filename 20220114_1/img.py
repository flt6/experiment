from matplotlib import pyplot as plt
from numpy import  array
x=[]
y=[]
with open("out.txt","r") as f:
    for i in f:
        t1,t2=i.split(" ")
        x.append(float(t1))
        y.append(float(t2))
# print(x,y)
plt.title("X-Y")
plt.plot(x, y,'.')
# plt.show(block=True)
plt.savefig("img.png",dpi=2000)
