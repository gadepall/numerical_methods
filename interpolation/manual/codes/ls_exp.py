import numpy as np
import matplotlib.pyplot as plt

x = np.matrix([0,2,4,
\
6,8])
y = np.matrix([5,4,1
\
,6,7])
ylog = np.log(y)
A = np.column_stack([x.T,np.ones([5,1])])
z = np.linalg.inv(A.T*A)*A.T*ylog.T
print(np.exp(z[0]),z[1])
yloghat=A*z
yhat = np.exp(yloghat)
x = np.array(x)[0]
y = np.array(y)[0]
yhat = np.array(yhat.T)[0]
plt.plot(x,yhat,label='estimate')
plt.plot(x,y,'o',label='data')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best', prop={'size':11})
#plt.savefig('../figs/ls_exp.eps')
plt.show()