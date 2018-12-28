# https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-5-lagend/
# https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt7_legend.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3, figsize=(8, 5)) # 以下是這張figure的數據

plt.xlim((-1, 2)) # x show limit range
plt.ylim((-2, 3)) # y show limit range
plt.xlabel('I am x') # show x name
plt.ylabel('I am y') # show y name

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks) # 替換x座標的範圍文字
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ good$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$']) # 替換y座標的範圍文字, r是正則表達式, $是變好看的字體, \alpha是數學符號

l1, = plt.plot(x, y2, label='up') # 傳進legend必須加前面','
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down') # 設定個別參數, 傳進legend必須加前面','
# plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best') # 圖例, loc='best'不會擋住數據
plt.legend(handles=[l1,], labels=['aaa',], loc='best') # 圖例, loc='best'不會擋住數據, 只會印出aaa那條圖例

plt.show()