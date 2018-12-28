# https://morvanzhou.github.io/tutorials/data-manipulation/plt/3-1-scatter/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt10_scatter.py
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()