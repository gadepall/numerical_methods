import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3 +x -1

def f1(x):
	return 3*x**2 + 1	

a = 1
n = 4
for i in range(n):
	a = a - f(a)/f1(a)

print(a)
