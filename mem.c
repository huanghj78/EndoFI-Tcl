#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor))
void load() {
    // 设置每次循环的时间间隔，单位为微秒
    const int INTERVAL = 10000; 
    // 设置程序的持续时间，单位为毫秒
    const int DURATION=20000; 
    // 设置目标内存消耗值，单位为MB
    const int TARGET_MEMORY=99999999999999;
    // 计算循环的次数
    const int LOOP_COUNT = DURATION * 1000 / INTERVAL; 
    // 设置程序达到目标内存消耗的时间，单位为毫秒
    const int RAMP_UP_TIME=10000; 
    // 计算达到目标内存消耗的次数
    const int RAMP_UP_COUNT = RAMP_UP_TIME * 1000 / INTERVAL; 
    // 设置每次申请的内存大小，单位为字节
    const long long CHUNK_SIZE = TARGET_MEMORY / RAMP_UP_COUNT * 1024 * 1024;
    int count = 0; //记录申请的内存块数
    char *p[999999]; //用于存储指向内存块的指针

    for (int i = 0; i < LOOP_COUNT; i++) { //循环申请内存，直到达到持续时间
        if (count*CHUNK_SIZE/1024/1024 < TARGET_MEMORY) { //如果还没有达到目标值且还在上升阶段
            p[count] = (char *)malloc(CHUNK_SIZE); //申请一块内存
            if (p[count] == NULL) { //判断是否申请成功
                for (int i = 0; i < count; i++) { //循环释放内存
                    free(p[i]); //释放一块内存
                }
                exit(1);
            }
            count++; //增加计数器
            // printf("已申请%lldMB内存\n", count*CHUNK_SIZE/1024/1024);
        }
        usleep(INTERVAL); //延迟一定的时间间隔
    }
    for (int i = 0; i < count; i++) { //循环释放内存
        free(p[i]); //释放一块内存
        usleep(INTERVAL);
    }
}