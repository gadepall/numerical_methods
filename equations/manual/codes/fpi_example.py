import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-5,5,20)
y = x**3+x-1
plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.savefig('../figs/fpi_example.eps')
plt.show()
