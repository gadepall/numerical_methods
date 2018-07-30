import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3 +x -1

a = -1
b = 1

n = 50

for i in range(n):
	c = (a + b)/2
	if f(c) < 0 :
		a = c
	else:
		b = c


print(c)
