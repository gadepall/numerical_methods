import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-x**2)

a = 0
b = 1
n = 11
m = int((n-1)/2)
x = np.linspace(a,b,n)
h = (b-a)/(n-1) 
odd_n = list(range(1,2*m+1,2))
even_n = list(range(2,2*m,2))

s0 = f(a) + f(b)
s1 = np.sum(f(x[odd_n]))
s2 = np.sum(f(x[even_n]))
J = h/3*(s0+4*s1+2*s2)
print(J)

