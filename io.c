#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h> // 导入系统调用函数所需的头文件
#include <fcntl.h> // 导入open函数所需的标志位

__attribute__((constructor))
void load() {
    int delta_ms=20000;
    int MAXBUFSIZE = 5000; // 缓冲区大小
    int fd1, fd2; // 文件描述符
    char buffer[MAXBUFSIZE]; // 缓冲区
    struct timeval start_tv;
    struct timeval end_tv;
    gettimeofday(&start_tv, NULL);
    gettimeofday(&end_tv, NULL);
    long long start_ts = start_tv.tv_sec*1000+start_tv.tv_usec/1000;
    long long end_ts = end_tv.tv_sec*1000+end_tv.tv_usec/1000;

    fd1 = open("/home/postgres/source", O_RDONLY);
    if (fd1 == -1) {
        perror("open source file failed");
        exit(1);
    }

    // 以追加写模式打开目标文件，如果不存在则创建
    fd2 = open("/home/postgres/dest", O_WRONLY | O_APPEND | O_CREAT, 0666);
    if (fd2 == -1) {
        perror("open dest file failed");
        exit(1);
    }

    while(end_ts - start_ts < delta_ms) {
        gettimeofday(&end_tv, NULL);
        end_ts = end_tv.tv_sec*1000+end_tv.tv_usec/1000;
        // 从源文件中读取MAXBUFSIZE个字节到缓冲区中
        int nread = read(fd1, buffer, MAXBUFSIZE);
        if (nread == -1) {
            perror("read source file failed");
            break;
        }
        if (nread == 0) {
            // 如果读到文件末尾，就重新定位到文件开头
            lseek(fd1, 0, SEEK_SET);
            continue;
        }

        // 将缓冲区中的内容写入到目标文件中
        int nwrite = write(fd2, buffer, nread);
        if (nwrite == -1) {
            perror("write dest file failed");
            break;
        }
        if (nwrite < nread) {
            // 如果写入的字节数小于读取的字节数，就重新定位到未写入的位置
            lseek(fd1, nwrite - nread, SEEK_CUR);
        }
    }

}
