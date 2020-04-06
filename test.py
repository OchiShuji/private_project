import math
import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(-np.pi, np.pi, 100)
r = np.sin(theta)*np.cos(theta) / ( (np.sin(theta))**3 + (np.cos(theta))**3 )
polar = [r, theta]
rot = [np.cos(theta),-np.sin(theta),np.sin(theta),np.cos(theta)]
inv_rot = [np.cos(theta),np.sin(theta),-np.sin(theta),np.cos(theta)]
x = inv_rot[0] * polar[0] + inv_rot[1] * polar[1]
y= inv_rot[2] * polar[0] + inv_rot[3] * polar[1]
plt.plot(x,y)
plt.show()
