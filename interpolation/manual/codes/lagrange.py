#Forward differences coefficients
#for Newton's Interpolation Formula
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
	
x = np.array([9.3,9.6,10.2,
\
10.4,10.8])
y = np.array([11.4,12.8,14.7
\
,17,19.8])

poly = lagrange(x, y)
p = Polynomial(poly).coef
print(np.polyval(p,10))




