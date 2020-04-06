import numpy as np
from matplotlib import pyplot as plt 

n_max = int(input("n=")) + 1
N =  1000
x = np.linspace(-1.5*np.pi,1.5*np.pi,N)

val = np.zeros(N)
for i in range(1,n_max):
    val = val + 2 * (-1)**(i+1) * np.sin(i*x) / i

val_origin = np.zeros(N)
for i in range(1,10000):
    val_origin = val_origin + 2 * (-1)**(i+1) * np.sin(i*x) / i

plt.plot(x,val,linewidth=1)
plt.plot(x,val_origin,linewidth=1,color="gray",linestyle="--")
plt.title("n={}".format(n_max-1))
plt.xticks([-1.5*np.pi,-1.0*np.pi,-0.5*np.pi,0,0.5*np.pi,1.0*np.pi,1.5*np.pi],[r"$-\frac{3}{2}\pi$",r"$-\pi$",r"$-\frac{1}{2}\pi$",r"$0$",r"$\pi$",r"$\frac{1}{2}\pi$",r"$\frac{3}{2}\pi$"])
plt.show()