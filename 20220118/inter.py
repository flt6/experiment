from matplotlib import pyplot as plt
f=open("FAccelerometer.csv","r")
f.readline()

ax=[]
ay=[]
for i in f:
    _,x,y,_=i.split()
    ax.append(float(x))
    ay.append(float(y))

f,(a,b)=plt.subplots(2,1,sharey=True,sharex=True)

a.plot(ax,".")
b.plot(ay,".")

f.show()
plt.show(block=True)