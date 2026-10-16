#include <stdint.h>
#include <stdio.h>
double f(n)
{
    if (n<10) {
    return 3;
    } else {
        return (n+4)*f(n-5);
    }
}

int main (void) {
    double res = (f(257487)/683 + 67*f(257477))/f(257472);
printf("%d",res);
}
