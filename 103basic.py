# https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-1-basic-usage/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt3_simple_plot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50) # 從-1~1, 有50個點
# y = 2*x+1
y = x**2
plt.plot(x, y)
plt.show()