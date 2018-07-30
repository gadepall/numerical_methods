import numpy as np

def f(x):
	return np.exp(-x**2)

a = 0
b = 1

deg = 3
t, w = np.polynomial.legendre.leggauss(deg)
x = 0.5*(t + 1)*(b - a) + a
J = np.sum(w * f(x))* 0.5*(b - a)
print(J)

