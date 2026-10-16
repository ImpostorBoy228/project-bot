#include <stdio.h>
int f(int x, int y) {
    if (x>y) {return 0;}
    if (x==y) {return 1;}
    if (x==6 || x==12) {return 0;}
    return f(x+1,y)+f(2*x,y)+f(x+3,y);
}
int main(void) {printf("%d",f(3,16));}
