import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
	return 1-x*y


a = 0
b = 5
n = 25
x = np.linspace(a,b,n)
h = (b-a)/(n+1) #interval
y=[]
tempy = 1
for i in range(n):
	y.append(tempy)
	k1 = f(x[i],tempy)
	k2 = f(x[i]+h/2,tempy+ h*k1/2)
	k3 = f(x[i]+h/2,tempy+h*k2/2)
	k4 = f(x[i]+h,tempy+h*k3)	
	tempy = tempy + h/6*(k1+2*k2+2*k3+k4)	

#Plotting
plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')

#Comment the following line
plt.savefig('../figs/runge.eps')
plt.show()

