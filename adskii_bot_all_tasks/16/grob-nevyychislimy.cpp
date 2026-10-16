#include "/home/impostorboy/projects/deez/src/nut.hpp"
#include <cmath>
#include <iostream>

Nut f(Nut n) {
    if (n.num/n.den<10) {return n;}
    if ((n.num/n.den)%2==0) {return f(nutmake((n.num/n.den)%10))+f(nutmake((n.num/n.den)/10));}
    return (f(nutmake(std::pow(10,(n.num/n.den))))+f(nutmake((n.num/n.den)%10))-nutmake(2));
}

int main() {
    int c;
    for (int i = 0;i<std::pow(10,11);i++) {
        Nut n = f(nutmake(i));
        if(n.num/n.num==0) {c++;}
    }
    std::cout << c << std::endl;
}
