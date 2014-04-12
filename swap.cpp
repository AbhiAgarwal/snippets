#include <cstdio>
using namespace std;

// Header File
#define Swap(a, b) ((a) ^= (b), (b) ^= (a), (a) ^= (b))

// Function
void swap(int &a, int &b){
    b ^= a ^= b ^= a;
}

int main(void){
    int a = 1, b = 2;
    swap(a, b);
    printf("a: %d, b: %d\n", a, b);
}
