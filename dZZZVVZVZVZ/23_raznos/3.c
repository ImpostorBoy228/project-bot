#include <stdio.h>
int f(int x, int y) {
    if (x>y) {return 0;}
    if (x==y) {return 1;}
    return f(x+1,y)+f(3*x,y)+f(2+x,y);
}
int main(void) {printf("%d",f(1,10)*f(10,12)*f(12,15));} // 89
