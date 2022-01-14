from matplotlib import pyplot as plt
l=[]
with open("data.csv","r") as f:
    for i in f:
        l.append([float(j) for j in i.split(',')])
pos=[]
xpos=[]
ypos=[]
x=0
y=0
z=0
vx=0
vy=0
vz=0
for _,ax,ay,az,_ in l:
    vx,vy,vz=vx+ax*0.01,vy+ay*0.01,vz+az*0.01
    # print("%f,%f,%f"%(ax,ay,az))
    x,y,z=x+vx*0.01,y+vy*0.01,z+vz*0.01
    xpos.append(x)
    ypos.append(y)
    pos.append([x,y,z])
with open("opt.csv",'w') as f:
    for i in pos:
        print(",".join([str(j) for j in i]),file=f)
plt.title("X-Y")
plt.plot(xpos, ypos)
plt.show(block=True)