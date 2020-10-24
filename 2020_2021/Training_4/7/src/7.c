#include <stdio.h>


char s [] = {100, 0, 0, 111, 0, 0, 110, 0, 0, 110, 0, 0, 117, 0, 0, 67, 0, 0, 84, 0, 0, 70, 0, 0, 123, 0, 0, 101, 0, 0, 97, 0, 0, 115, 0, 0, 121, 0, 0, 95, 0, 0, 99, 0, 0, 117, 0, 0, 115, 0, 0, 55, 0, 0, 48, 0, 0, 109, 0, 0, 95, 0, 0, 115, 0, 0, 116, 0, 0, 114, 0, 0, 99, 0, 0, 109, 0, 0, 112, 0, 0, 125, 0, 0, 0};


int custom_strcmp(char* s1, char* s2) {
    
    int i = 0;
    int j = 0;

    for (; s1[i] || s2[j]; i++, j = j + 3) {
        if (s1[i] - s2[j]) {
            return s1[i] - s2[j];
        }
    }

    return s1[i] - s2[j];
}


int main(int argc, char const * argv[]) {

    char f [29];
    printf("Enter the flag >> ");
    fgets(f, 29, stdin);
    
    if (!custom_strcmp(f, s)) {
        printf("Flag is correct\n");
        return 0;
    } else {
        printf("Flag is incorrect\n");
        return 0;
    }
}