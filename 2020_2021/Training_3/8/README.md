# 8

## Task

```C
#include <stdio.h>
#include <string.h>


char s [] = {23, 10, 13, 27, 7, 38, 63, 35, 2, 11, 85, 17, 42, 27, 8, 27, 9, 74, 30, 86, 13, 1, 19, 82, 90, 85, 23, 14, 0};

int t(int a, int b) {
    return (~a | ~b) & (a | b);
}

void process(char* k) {
    int a = strlen(s);
    int b = strlen(k);

    for (int i = 0; i < a; i++) {
        s[i] = t(s[i], k[i % b]);
    }
}

int main(int argc, char const *argv[]) {
    char input [10];
    printf("Enter the string >> ");
    fgets(input, 10, stdin);
    process(input);
    printf("Your flag is: %s\n", s);
}
```

## Solution