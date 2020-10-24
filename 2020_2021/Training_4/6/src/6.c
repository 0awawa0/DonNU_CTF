#include <stdio.h>


int main(int argc, char const * argv[]) {
    
    char a, b, c;
    printf("Give me a string >> ");
    scanf("%c", &a);
    scanf("%c", &b);
    scanf("%c", &c);

    if (a > b || b < c || a < c) {
        printf("No flag for you\n");
        return 1;
    }

    if (a * b * c != 146969) {
        printf("No flag for you\n");
        return 1;
    }

    printf("Flag is donnuCTF{%d_%d_%d}\n", c, b, a);
    return 0;
}