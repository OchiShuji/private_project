import numpy as np 
from matplotlib import pyplot as plt 

n = int(input("#iteration"))
a = np.linspace(0.0,1.0,n)
b = np.linspace(1.0,0.0,n)
for i in range(0,n):
    x = np.linspace(-a[i],a[i],256)
    print(a[i])
    y_plus = b[i]*np.sqrt(1-x**2/a[i]**2)
    y_minus = -b[i]*np.sqrt(1-x**2/a[i]**2)
    plt.plot(x,y_plus,linewidth=0.5,color="r")
    plt.plot(x,y_minus,linewidth=0.5,color="r")
plt.show()