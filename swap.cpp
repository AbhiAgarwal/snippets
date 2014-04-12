#include <cstdio>
using namespace std;

void swap(int &a, int &b){
    b ^= a ^= b ^= a;
}

int main(void){
    int a = 1, b = 2;
    swap(a, b);
    printf("a: %d, b: %d\n", a, b);
}
