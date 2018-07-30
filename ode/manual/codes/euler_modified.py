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
	tempy = tempy + h*(1-x[i]*tempy)

#Plotting
plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')

#Comment the following line
plt.savefig('../figs/euler_modified.eps')
plt.show()

