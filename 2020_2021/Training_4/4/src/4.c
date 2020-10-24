#include <stdio.h>
#include <string.h>


char s  [] = {100, 15, 111, 49, 110, 61, 110, 80, 117, 30, 67, 89, 84, 102, 70, 40, 123, 10, 116, 89, 97, 102, 107, 3, 51, 9, 95, 11, 111, 32, 110, 45, 49, 57, 121, 80, 95, 12, 51, 144, 118, 34, 51, 52, 110, 103, 95, 98, 110, 35,  117, 65, 109, 82, 115, 39, 125, 84, 0};


int main(int argc, char const *argv[]) {
    char f [30];
    printf("Enter the flag >> ");
    fgets(f, 30, stdin);

    for (int i = 0, j = 0; s[i]; i = i + 2, j++) {
        if (s[i] != f[j]) {
            printf("You are wrong!\n");
            return 1;
        }
    }
    printf("Flag is correct!\n");
    return 0;
}