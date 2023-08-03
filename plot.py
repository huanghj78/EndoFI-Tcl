# 导入matplotlib库
import matplotlib.pyplot as plt

# 定义两组数据，分别表示x轴和y轴的坐标
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 使用scatter函数绘制散点图
plt.scatter(x, y)

# 设置标题和坐标轴标签
plt.title("Scatter Plot Example")
plt.xlabel("x")
plt.ylabel("y")

# 显示图形
plt.show()
