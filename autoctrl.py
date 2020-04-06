import numpy as np 
from matplotlib import pyplot as plt 

t = np.linspace(0 ,100, 10000)
x = 12 * (4 - t**2) / ((4 - t**2)**2 + 4*(t**2))
y = 12 * (-2*t) / ((4 - t**2)**2 + 4*(t**2))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(x,y)
plt.show()
