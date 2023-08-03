import os
import sys
import yaml

FAULT_TYPE = ['cpu', 'io', 'mem', 'lock', 'slow_sql']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py file_path")
        exit()
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    fault_type = data['type']
    args = data['args']
    ip = data['client']['ip']
    port = data['client']['port']
    duration = data['duration']
    sql_filter = data['filter']
    pid = data['pid']
    print(pid)
    arg = ""

    if fault_type not in FAULT_TYPE:
        print("Invalid fault type")
        exit()
    
    if fault_type == "cpu":
        os.system("cp inject-template/cpu-template cpu.cpp")
        os.system(f"sed -i \"s/int TARGET_CPU_USAGE/int TARGET_CPU_USAGE={args['cpu_usage']}/g\" cpu.cpp")
        os.system(f"sed -i \"s/int DURATION/int DURATION={duration}/g\" cpu.cpp")
        os.system(f"sed -i \"s/int RAMP_UP_TIME/int RAMP_UP_TIME={args['slope_time']}/g\" cpu.cpp")
        # os.system("clang -ggdb -D_GNU_SOURCE -shared -o inject.so -fPIC cpu.cpp")
        os.system("g++ -shared -o inject.so -fPIC cpu.cpp")
        # 将注入的动态库拷贝到GaussDB进程所能访问的路径下
        os.system("cp inject.so /home/postgres")
        # os.system("docker cp inject.so gs-dev:/home/opengauss")
        # os.system("rm cpu.cpp inject.so")
    elif fault_type == "io":
        os.system("cp inject-template/io-template io.c")
        os.system(f"sed -i \"s/int delta_ms/int delta_ms={duration}/g\" io.c")
        os.system("clang -std=gnu99 -ggdb -D_GNU_SOURCE -shared -o inject.so -fPIC io.c")
        # os.system("gcc -shared -o inject.so -fPIC io.c")
        # os.system("docker cp inject.so gs-dev:/home/opengauss")
        # os.system("rm io.c inject.so")
        # 通过对source文件进行复制模拟IO高负载
        # os.system("docker cp source gs-dev:/home/opengauss")
        os.system("cp inject.so /home/postgres")
    elif fault_type == "mem":
        os.system("cp inject-template/mem-template mem.c")
        os.system(f"sed -i \"s/int TARGET_MEMORY/int TARGET_MEMORY={args['size']}/g\" mem.c")
        os.system(f"sed -i \"s/int DURATION/int DURATION={duration}/g\" mem.c")
        os.system(f"sed -i \"s/int RAMP_UP_TIME/int RAMP_UP_TIME={args['slope_time']}/g\" mem.c")
        os.system("clang std=gnu99 -ggdb -D_GNU_SOURCE -shared -o inject.so -fPIC mem.c")
        # os.system("docker cp inject.so gs-dev:/home/opengauss")
        # os.system("rm mem.c inject.so")
        os.system("cp inject.so /home/postgres")
    elif fault_type == "lock":
        arg = args['relation_id']
    
    os.system(f"./run.sh {ip} {port} {fault_type} {duration} {sql_filter} {pid} {arg}")


