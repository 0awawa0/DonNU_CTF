#include <stdio.h>


int main(int argc, char const * argv[]) {
    
    int a, b, c;
    printf("Enter a >> ");
    scanf("%d", &a);
    printf("Enter b >> ");
    scanf("%d", &b);
    printf("Enter c >> ");
    scanf("%d", &c);

    if (a == 89 && b == 43 && c == 103) {
        printf("Flag is donnuCTF{%c_%c_%c}\n", b, a, c);
    } else {
        printf("No flag for you\n");
    }

    return 0;
}