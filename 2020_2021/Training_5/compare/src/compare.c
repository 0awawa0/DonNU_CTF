#include <stdio.h>
#include <string.h>

int main() {
    char input[256];

    printf("Enter flag to check: ");
    scanf("%s", input);
    if (strlen(input) != 10) {
        printf("Wrong length!\n");
        return 0;
    }
    if (strcmp(input, "s33_c10sed") <= 0) {
        printf("Wrong check 1!\n");
        return 0;
    }
    if (strcmp(input, "s33_c10sef") >= 0) {
        printf("Wrong check 2!\n");
        return 0;
    }
    printf("Your flag is donnuCTF{%s}\n", input);
    return 0;
}
