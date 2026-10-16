#include "common.h"
#include <stdbool.h>

int g(int s,int x) {
    if (s>=67) {
        return x%2==0;
    }
    int m[2]={g(s*3,x+1),g(s+1,x+1)};
    if (x%2!=0) {
        return all(m,2);
    } else {
        return any(m,2);
    }

}

int main(){
    for (int i=0;i<150;i++) {
        printf("%d",g(i,1));
    }
}
