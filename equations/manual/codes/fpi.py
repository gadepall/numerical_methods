import numpy as np
import matplotlib.pyplot as plt

def g(x):
	return 1/(1+x**2)

a = 1
n = 50
for i in range(n):
	a = g(a)

print(a)

