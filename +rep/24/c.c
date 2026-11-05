#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE* f = fopen("./24_10", "r"); 

    if (f == NULL) {
        goto nafig;
    }

    int c;
    int index=0;
    int* p = malloc(sizeof(int) * 1000000);
    int psize=0;
    int da = 0;
    while (c = fgetc(f) != EOF) {
        if (c=='T') {
            p[psize++] = index;
            if (da) {
                
            }
        }
        index++;
    }

nafig:
    fclose(f);
    return 666;
}
