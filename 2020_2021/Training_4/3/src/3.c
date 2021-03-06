#include <stdio.h>
#include <string.h>

char s [] = {100, 111, 110, 110, 117, 67, 84, 70, 123, 103, 108, 48, 98, 97, 108, 95, 102, 49, 97, 103, 95, 97, 114, 114, 97, 121, 125, 0};


int main(int argc, char const *argv[]) {
    char f [28];
    printf("Enter a flag >> ");
    fgets(f, 28, stdin);

    if (!strcmp(f, s)) {
        printf("Flag is correct\n");
    } else {
        printf("Flag is incorrect\n");
    }
}
