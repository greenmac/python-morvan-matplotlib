# https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-2-figure/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt4_figure.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

plt.figure() # 以下是這張figure的數據
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5)) # 以下是這張figure的數據
plt.plot(x, y2) 
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--') # 設定個別參數


plt.show()