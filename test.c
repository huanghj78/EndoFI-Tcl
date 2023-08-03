// #include <stdlib.h>
// #include <time.h>
// __attribute__((constructor))
// void load() {
// 	int i = 0;
// 	char* p[10];
// 	while(1){
// 		if(i == 10) {
// 			break;
// 		}
// 		p[i] = (char *)malloc(1024*1024*100);
// 		i++;
// 		sleep(1);
// 	}
// 	sleep(10);
// 	for(i = 0; i < 10; i++){
// 		sleep(1);
// 		free(p[i]);
// 	}

// }
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MB (1024*1024)

int main() {
    int i;
    char *buffer;
    for (i = 0; i < 100; i++) {
        buffer = malloc(MB); // 分配1MB的内存
        if (buffer == NULL) {
            printf("Out of memory\n");
            exit(1);
        }
        printf("Allocated %d MB\n", i+1);
        buffer[0] = 'a'; // 写入第一个字节
        printf("First byte: %c\n", buffer[0]); // 读取第一个字节
        sleep(1); // 暂停1秒
    }
    return 0;
}

