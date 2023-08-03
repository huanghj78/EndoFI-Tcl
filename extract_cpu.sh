#!/bin/bash
cd samples
# 假设数据存储在data.txt文件中
file_name=$1
input_file=$file_name
output_file=$file_name".csv"

rm $output_file
# 初始化输出文件
# echo "CPU Usage" > $output_file

# 初始化标记变量
found_cpu_line=false

# 读取输入文件中的每一行
while IFS= read -r line; do
    # 检查当前行是否包含%CPU信息
    if [[ $line == *"%CPU"* ]]; then
        # 如果当前行包含%CPU信息，则设置标记变量为true
        found_cpu_line=true
    elif $found_cpu_line; then
        # 如果标记变量为true，则提取%CPU值
        cpu_usage=$(echo $line | awk '{print $9}')
        # 检查%CPU值是否为空
        if [[ -z "$cpu_usage" ]]; then
            # 如果%CPU值为空，则退出循环
            break
        else
            # 如果%CPU值不为空，则将其追加到输出文件中
            echo $cpu_usage >> $output_file
        fi
        # 重置标记变量为false
        found_cpu_line=false
    fi
done < $input_file
