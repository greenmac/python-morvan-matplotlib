# https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-4-axis2/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt6_ax_setting2.py
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

# gca = 'get current axis' 把現在的軸拿出來
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom') # 用哪個軸代替X軸
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]
ax.spines['bottom'].set_position(('data', 0))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data

ax.yaxis.set_ticks_position('left') # 用哪個軸代替Y軸
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]
ax.spines['left'].set_position(('data',0))

plt.show()