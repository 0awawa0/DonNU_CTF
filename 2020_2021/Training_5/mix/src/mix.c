#include <stdio.h>
#include <stdlib.h>

int main() {
    char input[256];
    char s[] = "mjzhhdozg|:WbRR";
    int i;

    printf("Enter flag to check: ");
    scanf("%s", input);
    for (i = 0; i < 15; i++) {
        if (input[i] + i != s[i]) {
            printf("Wrong position %d!\n", i);
            return 0;
        }
    }
    printf("Yes! Correct flag is donnuCTF {%s}\n", input);
    return 0;
}
