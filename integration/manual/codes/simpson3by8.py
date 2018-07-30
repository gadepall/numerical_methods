import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-x**2)

a = 0
b = 1
n = 31
m = int((n-1)/3)
x = np.linspace(a,b,n)
h = (b-a)/(n-1) 
one_m = list(range(1,3*m+1,3))
two_m = list(range(2,3*m+2,3))
three_m = list(range(3,3*m,3))

s0 = f(a) + f(b)
s1 = np.sum(f(x[one_m]))
s2 = np.sum(f(x[two_m]))
s3 = np.sum(f(x[three_m]))
J = 3*h/8*(s0+3*s1+3*s2 +2*s3)
print(J)

