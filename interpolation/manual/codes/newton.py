#Forward differences coefficients
#for Newton's Interpolation Formula
import numpy as np
from scipy.misc import comb
import mpmath as mp


def diff_f(n,y):
	k = np.asarray(range(n+1))
	coeff = comb(n,k)	
	return np.sum(coeff*(-1)**(n-k)*y[0:n+1])
	

x = np.array([0,0.001,0.002,
\
0.003,0.004,0.005])
y = np.array([1.121,1.123,1.1255
\
,1.127,1.128,1.1285])
n = 5
u = 4.5
ans = 0
for k in range(n+1):
	ans += diff_f(k,y)*mp.binomial(u,k)
	
print(ans)	


