#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h> // 导入系统调用函数所需的头文件
#include <fcntl.h> // 导入open函数所需的标志位

// 定义一个函数，用于生成一个指定大小的随机文件
void generate_random_file(char *filename, int size) {
    // 打开文件，如果不存在则创建
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file %s\n", filename);
        exit(1);
    }
    // 生成随机数据并写入文件
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        char c = rand() % 256;
        fwrite(&c, 1, 1, fp);
    }
    // 关闭文件
    fclose(fp);
}

// 定义一个函数，用于读取一个指定文件的内容，并输出到另一个文件
void read_file(char *filename, char *output) {
    // 打开输入文件，如果不存在则报错
    FILE *fp_in = fopen(filename, "r");
    if (fp_in == NULL) {
        printf("Error opening file %s\n", filename);
        exit(1);
    }
    // 打开输出文件，如果不存在则创建
    FILE *fp_out = fopen(output, "w");
    if (fp_out == NULL) {
        printf("Error opening file %s\n", output);
        exit(1);
    }
    // 读取输入文件内容并写入输出文件
    char c;
    while (fread(&c, 1, 1, fp_in) == 1) {
        fwrite(&c, 1, 1, fp_out);
    }
    // 关闭文件
    fclose(fp_in);
    fclose(fp_out);
}

// 定义一个函数，用于删除一个指定文件
void delete_file(char *filename) {
    // 删除文件，如果失败则报错
    if (remove(filename) != 0) {
        printf("Error deleting file %s\n", filename);
        exit(1);
    }
}

// 定义一个函数，用于在指定时间内让IO利用率上升，并输出到一个文件，最后把输出的文件也删掉
void increase_io_utilization(int duration) {
    // 获取当前时间戳
    time_t start = time(NULL);
    // 循环执行以下操作，直到达到指定时间
    while (time(NULL) - start < duration) {
        // 生成一个随机文件名和大小
        char source_filename[20];
        char dest_filename[20];
        sprintf(source_filename, "src_%d.txt", rand());
        sprintf(dest_filename, "dst_%d.txt", rand());
        int size = rand() % 1000000 + 1000000;
        // 生成随机文件
        generate_random_file(source_filename, size);
        generate_random_file(dest_filename, size);
        // 读取随机文件并输出到指定文件
        read_file(source_filename, dest_filename);
        // 删除随机文件
        delete_file(source_filename);
        delete_file(dest_filename);
    }
}

// 主函数，接受两个命令行参数作为指定时间（秒）和输出的文件名
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s duration\n", argv[0]);
        exit(1);
    }
    int duration = atoi(argv[1]);
    increase_io_utilization(duration);
    return 0;
}
