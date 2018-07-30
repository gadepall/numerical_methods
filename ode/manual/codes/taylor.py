import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 5
n = 25
x = np.linspace(a,b,n)
h = (b-a)/(n+1) #interval
y=[]
tempy = 1
for i in range(n):
	y.append(tempy)
	yn1 = 1 - x[i]*tempy
	yn2 = -x[i]*yn1 -tempy
	yn3 = -x[i]*yn2 - 2*yn1 
	tempy = tempy + yn1*h+yn2*h**2/2 + yn3*h**3/6

#Plotting
plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')

#Comment the following line
#plt.savefig('../figs/taylor.eps')
plt.show()

