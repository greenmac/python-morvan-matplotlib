# https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-3-axis1/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt5_ax_setting1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3, figsize=(8, 5)) # 以下是這張figure的數據
plt.plot(x, y2) 
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--') # 設定個別參數

plt.xlim((-1, 2)) # x show limit range
plt.ylim((-2, 3)) # y show limit range
plt.xlabel('I am x') # show x name
plt.ylabel('I am y') # show y name

# show new ticks
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks) # 替換x座標的範圍文字
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ good$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$']) # 替換y座標的範圍文字, r是正則表達式, $是變好看的字體, \alpha是數學符號

plt.show()