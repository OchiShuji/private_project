import numpy as np 
from matplotlib import pyplot as plt 

class NacaFourdigit:
    param = ""
    params = []
    r_t = 0.0

    def __init__(self,param):
        if isinstance(param,str):
            self.param = param
            m = param[0]
            p = param[1]
            t = param[2:]
            try:
                m = float(m) * 0.01
                p = float(p) * 0.1
                t = float(t) * 0.01
            except ValueError:
                print("Error : Incorrect Numbering")
            self.params.append(m)
            self.params.append(p)
            self.params.append(t)
        else:
            pass        

    def t_distribution(self,x):
        '''Calculate thickness distribution of the wingsection'''
        t = self.params[2]
        y_t = t/0.20*(0.29690*np.sqrt(x)-0.12600*x-0.35160*x**2+0.28430*x**3-0.10150*x**4)
        return y_t

    def LE_radius(self):
        '''Leading edge radius of the wingsection'''
        self.r_t = 1.1019*self.params[2]**2
        return self.r_t
    
    def camber_line(self,x):
        '''Calculate a camber line of the wingsection'''
        m = self.params[0]
        p = self.params[1]
        N = len(x)
        y_c = np.zeros(N)
        for i in range(0,N):
            if x[i] <= p:
                y_c[i] = m*(2*p*x[i]-x[i]**2)/p/p
            else:
                y_c[i] = m*((1-2*p)+2*p*x[i]-x[i]**2)/(1-p)/(1-p)
        return y_c
    
    def wingsection(self,x):
        '''Calculate coordinates of upper and lower surface of the wingsection'''
        m = self.params[0]
        p = self.params[1]
        N = len(x)
        theta = np.zeros(N)
        y_t = self.t_distribution(x)
        y_c = self.camber_line(x)
        x_u,y_u,x_l,y_l = np.zeros(N),np.zeros(N),np.zeros(N),np.zeros(N)
        for i in range(0,N):
            if x[i] <= p:
                theta[i] = np.arctan(m*(2*p-2*x[i])/p/p)
            else:
                theta[i] = np.arctan(m*(2*p-2*x[i])/(1-p)/(1-p))
            x_u[i] = x[i] - y_t[i]*np.sin(theta[i])
            y_u[i] = y_c[i] + y_t[i] * np.cos(theta[i])
            x_l[i] = x[i] + y_t[i]*np.sin(theta[i])
            y_l[i] = y_c[i] - y_t[i] * np.cos(theta[i])
        return x_u,y_u,x_l,y_l

    def print_params(self):
        '''Print each parameters of the wingsection'''
        print("NACA",self.param,"4-digit wingsection")
        print("m=",self.params[0])
        print("p=",self.params[1])
        print("t=",self.params[2])

    def export(self,x):
        '''Export coordinates as csv'''
        import csv
        file_name = "NACA" + self.param + ".csv"
        f = open(file_name,"w")
        w = csv.writer(f)
        w.writerow(["x","y_c","x_u","y_u","x_l","y_l"])
        N = len(x)
        y_c = self.camber_line(x)
        x_u,y_u,x_l,y_l = self.wingsection(x)
        for i in range(0,N):
            w.writerow([np.round(x[i],4),np.round(y_c[i],4),np.round(x_u[i],4),np.round(y_u[i],4),np.round(x_l[i],4),np.round(y_l[i],4)])
        f.close()


class NacaFivedigit:
    pass

wing1 = NacaFourdigit("2412.5")
x = np.linspace(0,1,100)
x_u,y_u,x_l,y_l = wing1.wingsection(x)
wing1.export(x)
plt.plot(x_u,y_u)
plt.plot(x_l,y_l)
plt.show()