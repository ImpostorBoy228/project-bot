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
    while ((c = fgetc(f)) != EOF) {
        if (c == 'T') {
            p[psize++] = index;
        }
        index++;
    }

    int* rast = malloc(sizeof(int) * 1000000);
    int rastsize = 0;
    int rr=0;
    for (int y=0;y<psize;++y) {
        rr++;
        if (y==psize-1) {
            continue;
        }
        if (p[y+1] == p[y]+1) { // мы стоим на начале tt 
            rast[rastsize++]=rr;
            rr=0;
            y++;
        }
    }

    int min=0;
    for (int i=0;i<=149;++i) {
        min+=rast[i]; 
    }

    int d = min;
    for (int l=150; l<rastsize; ++l) {
        d = d - rast[l-150]+rast[l];
        min = (min > d) ? d : min;
    }
    printf("%d", min);

nafig:
    if (f) fclose(f);
    return 666;
}
