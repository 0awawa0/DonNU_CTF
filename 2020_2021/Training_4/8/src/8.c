#include <stdio.h>


int f(int k) {

    int a0 = 0;
    int a1 = 1;
    int s = a0 + a1;

    for(int i = 2; i < k; i++) {
        a0 = a1; 
        a1 = s;
        s = a0 + a1;
    }

    return s;
}

int main(int argc, char const * argv[]) {

    int c;
    printf("Enter a number >> ");
    scanf("%d", &c);
    if (f(17) == c) {
        printf("Flag is donnuCTF{0x%04x}\n", c);
    } else {
        printf("No flag for you!\n");
    }
    return 0;
}