import numpy as np 
from matplotlib import pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-np.sqrt(5),np.sqrt(5),100000)
f = np.sqrt(np.abs(x)) + np.sqrt(5-x*x)
g = np.sqrt(np.abs(x)) - np.sqrt(5-x*x)

fig = plt.figure()
ims1,ims2 = [],[]
for n in range(0,100):
    angle =  np.sin(2*np.pi*n/100)
    x_angle = x * angle
    im1 = plt.plot(x_angle,f,x_angle,g,color="red")
    plt.xticks([-3,-2,-1,0,1,2,3])
    ims1.append(im1)
ani1 = animation.ArtistAnimation(fig,ims1,interval = 50)
plt.show()
