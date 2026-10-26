#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>

int main(void) {
    FILE* f = fopen("24var01.txt", "r"); if (f==NULL) goto nafig;
    char ass[5000000+1]; // переносим в ужасно быстрый стек (ass это 5 мб так что норм)
    fgets(ass, sizeof ass, f);
    
    uint_fast32_t maxcount = 0;
    for (uint_fast32_t in=0; in<5000000+1;++in) {
        char first = ass[in];
        if (first!='S') continue;
        uint_fast32_t numcount = 0; // страшно быстро

        for (uint_fast32_t j = in+1; j<5000000 && ass[j]!='S' && ass[j]!='\0'; ++j) {
            char current = ass[j];
            current = ass[j];
            if (isdigit(current)) {
                int toint = current - '0';
                if (toint%2==1) {
                    ++numcount;
                }
                if (++numcount == 35) {
                    maxcount = (maxcount>(j-in+1)) ? maxcount : (j-in+1) ;
                } else if (numcount > 35) { // на всякий случай
                    break;                
                }
            }
        }
    }
    
    printf("%" PRIuFAST32 "\n", maxcount);

nafig: // используем уникальные фичи C
    fclose(f);
    return 666;
}
