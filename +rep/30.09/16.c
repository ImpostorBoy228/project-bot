#include <stdio.h>

int g(int n ) {
    if (n<10) {
        return 2*n;
    } else {
        return g(n-2)+1;
    }
}

int f(int n){
    return 2*(g(n-3)+8);
}

int main(void) {
    printf("%d",f(15548));
}
