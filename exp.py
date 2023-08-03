import os
import subprocess
import time

# 开启一个进程，切换到用户postgres，然后执行pgbench -T60
subprocess.Popen("sudo -u postgres /usr/local/postgresql/bin/pgbench -T60", shell=True)

# 过40秒之后，开启另一个进程执行以下指令
time.sleep(30)
pid = subprocess.check_output("ps aux | grep \"postgres: postgres postgre[s]\" | awk '{print $2}'", shell=True).decode().strip()
subprocess.Popen(f"sed -i 's/pid: .*/pid: {pid}/' /root/gdb-dbfi/pgsql/config/cpu.yaml", shell=True)
subprocess.Popen(f"python3 /root/gdb-dbfi/pgsql/main.py /root/gdb-dbfi/pgsql/config/cpu.yaml", shell=True)

