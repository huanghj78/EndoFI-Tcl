# 导入需要的模块
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取csv文件
df = pd.read_csv("./results/result-mcd.csv")
print(df.shape)
# 获取x, y, z的值
X = np.array([1, 5, 10, 20])  # x是行索引
Y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # y是列索引
Z = np.ravel(df.values)  # z是表格中的数值，并转换为一维数组
# print(auc)
xx, yy = np.meshgrid(X, Y)
X, Y = xx.ravel(), yy.ravel()
bottom = np.zeros_like(X)
width = height = 1  # 每一个柱子的长和宽
fig = plt.figure()
ax = fig.gca(projection='3d')  # 三维坐标轴
ax.bar3d(X, Y, bottom, width, height, Z, shade=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z(value)')
plt.show()
