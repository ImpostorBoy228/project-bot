#include <stdio.h>
int f(int x, int y) {
    if (x>y) {return 0;}
    if (x==y) {return 1;}
    return f(x+1,y)+f(2*x+1,y)+f(2*x,y)+f(x*10,y);
}
int main(void) {printf("%d",f(1,15));}
