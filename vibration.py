import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation 

N = 50
n = 10
dt = 0.08
T = 80
rho = 2700
A = 0.01
l = 1.0
P = 1000
E = 70*10**9
x = np.linspace(0,l,n)
t = np.arange(0.0,T,dt)

def U(i,x):
    return np.sqrt(2/rho/A/l)*np.sin((2*i-1)/2/l*np.pi*x)

def xi(i,t):
    ome = (2*i-1)/2/l*np.pi*np.sqrt(E/rho)
    return P/E/A*np.sqrt(2*rho*A/l)*4*l*l/(2*i-1)**2/np.pi**2*(-1)**(i-1)*np.cos(ome*t)

def u(x,t,N):
    u = 0.0
    for i in range(0,N):
        u = u + U(i,x)*xi(i,t)
    return u


imgs1 = []
#imgs2 = []
fig = plt.figure()

for tau in t:
    u_0 = np.zeros(n)
    for i in range(0,n):
        u_0[i] = u(x[i],tau,N)
    img1 = plt.plot(x+10000*u_0,np.zeros(n),marker='o',color="black")
    #img2 = plt.plot(x+10000*u_0,0.1*np.ones(n),marker='o',color="black")
    imgs1.append(img1)
    #imgs2.append(img2)

anm1 = animation.ArtistAnimation(fig,imgs1,interval=dt*1000,repeat=False)
#anm2 = animation.ArtistAnimation(fig,imgs2,interval=dt*1000,repeat=False)
plt.show()
