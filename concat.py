# 导入csv库
import csv

# 打开a.csv和b.csv文件，使用with语句自动关闭文件
with open("./samples/ad-cpu2.csv", "r") as a, open("./samples/ad-io2.csv", "r") as b:
    # 创建reader对象，用来读取每一行的数据
    reader_a = csv.reader(a)
    reader_b = csv.reader(b)
    # 将两个reader对象转换为列表，并使用zip函数按列合并
    data = zip(list(reader_a), list(reader_b))

# 打开c.csv文件，使用with语句自动关闭文件
with open("sample1.csv", "w") as c:
    # 创建writer对象，用来写入每一行的数据
    writer = csv.writer(c)
    # 遍历合并后的数据，将每一对数据拼接为一行，并写入c.csv文件
    for row_a, row_b in data:
        writer.writerow(row_a + row_b)
