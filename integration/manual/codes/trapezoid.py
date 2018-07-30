import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-x**2)

a = 0
b = 1
n = 11
x = np.linspace(a,b,n)
h = (b-a)/(n-1) 

J = h/2*(f(x[0])+2*np.sum(f(x[1:(n-2)]))+f(x[n-1]))
print(J)

