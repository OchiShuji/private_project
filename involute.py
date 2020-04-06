import numpy as np 
from matplotlib import pyplot as plt 

a = int(input("a="))
theta = np.linspace(0, 3*np.pi, 1000)
x = a * (np.cos(theta)+theta*np.sin(theta))
y = a * (np.sin(theta)-theta*np.cos(theta))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(x,y)
plt.show()