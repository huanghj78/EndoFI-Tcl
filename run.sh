#!/usr/bin/expect -f

# 读取参数
set ip [lindex $argv 0]
set port [lindex $argv 1]
set type [lindex $argv 2]
set sleep_time [lindex $argv 3]
set filter [lindex $argv 4]
set pid [lindex $argv 5]
set arg [lindex $argv 6]


puts $filter
puts $type
puts $pid
# 获取opengauss进程号并进行GDB初始化
# set pid [exec sh -c {ps aux|grep "/home/opengauss/openGauss/install/bin/gaussdb -D /home/opengauss/openGauss/dat[a]" | awk '{print $2}'}]
set timeout -1
spawn  gdb -p ${pid}
# 保证expect读取的输出时序正常
# expect "(gdb)" {sleep 0.1; send "\n"}
# expect "(gdb)" {send "set scheduler-locking off\n"}
# expect "(gdb)" {send "set print thread-events off\n"}
# expect "(gdb)" {send "handle SIGUSR1 noprint nostop pass\n"}
# expect "(gdb)" {send "handle SIGUSR2 noprint nostop pass\n"}

# 负载类型可无需匹配SQL语句直接注入
if {[string compare $type "cpu"] == 0 || [string compare $type "io"] == 0 || [string compare $type "mem"] == 0} {
    if {[string compare $filter "no"] == 0} {
        expect "(gdb)"
        send "print (int)dlclose((long long unsigned)dlopen(\"/home/postgres/inject.so\", 2))\n"
        expect "(gdb)"
        send "q\ny\n"
        exit
    }
}

# 找到目标线程编号
# set tid 0
# expect "(gdb)" {send "i threads\n"}
# expect "(gdb)" 
# set lines [split $expect_out(buffer) "\n"]
# set size [expr [llength $lines]-1]
# # worker线程起始下标
# set i 38 
# while {$i < $size} {
#     set thread_num [expr $i-1]
#     send "thread $thread_num\n"
#     expect "(gdb)"
#     send "f 11\n"
#     expect "(gdb)"
#     send "print port->remote_host\n"
#     expect "(gdb)"
#     set remote_host [lindex [split $expect_out(buffer) "\""] 1]
#     send "print port->remote_port\n"
#     expect "(gdb)"
#     set remote_port [lindex [split $expect_out(buffer) "\""] 1]
#     if {[string compare $ip $remote_host] == 0 && [string compare $port $remote_port] == 0} {
#         set tid $thread_num
#         break
#     }
#     set i [expr $i+1]
# }   

# if {$tid == 0} {
#     puts "COULD NOT FIND THREAD"
#     exit
# }

# 找到线程之后对其设置断点获取SQL
send "b exec_simple_query\n"
expect "(gdb)"
send "c\n"
set i 0
# 匹配SQL，兜底100次
while {$i > -1} {
    # set i [expr $i + 1]
    expect "(gdb)" 
    set items [split $expect_out(buffer) ","]
    set query [lindex [split [lindex $items 1] "\""] 1]
    # 匹配成功，开始注入故障
    if {[string match $filter $query]} {
        # 负载过高类型
        if {[string compare $type "cpu"] == 0 || [string compare $type "io"] == 0 || [string compare $type "mem"] == 0} {
            send "print (int)dlclose((long long unsigned)dlopen(\"/home/postgres/inject.so\", 2))\n"
            expect "(gdb)"
            send "q\ny\n"
            break
        # 锁表类型
        } elseif {[string compare $type "lock"] == 0} {
            send "b lock.c:771\n"
            expect "(gdb)"
            send "c\n"
            while {1} {
                expect "(gdb)"
                set func [lindex [split $expect_out(buffer) "," ] 1]
                set relid [lindex [split $func "="] 1]
                if {[string compare $relid $arg] == 0} {
                    send "print lockmode=8\n"
                    expect "(gdb)"
                    send "c\n"
                    after $sleep_time
                    send "q\ny\n"
                    break
                } else {
                    send "c\n"
                }
            }
            break
        # 慢SQL类型
        } elseif {[string compare $type "slow_sql"] == 0} {
            after $sleep_time
            # 80% for 500 ms
            # send "print (int)dlclose((long long unsigned)dlopen(\"/home/postgres/inject.so\", 2))\n"
            # expect "(gdb)"
            # send "b instrument.c:155\n"
            # send "b backend_status.c:578\n"
            # expect "(gdb)"
            # send "c\n"
            # expect "(gdb)"
            # send "print current_timestamp+=1000000000\n"
            # expect "(gdb)"
            send "c\n"
            # send "q\ny\n"
            # break
        }
    }
    send "c\n"
}
if {$i > -1} {
    expect "(gdb)"
    send "q\ny\n"
}



