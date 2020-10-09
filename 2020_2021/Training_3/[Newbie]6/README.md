# 6

## Task

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int ln(int x) {

    int t = x;
    int l = 0;

    while (t) {
        t = t >> 1;
        l++;
    }

    return l;
}


void process(char* s, int x, int l) {

    int i = l - 1;
    int t = x;

    for (int i = l - 1; t; i--, t = t >> 1) {
        *(s + i) = (char)(49 ^ (t & 1));
    }
}

int main(int argc, char const *argv[]) {

    int x;
    printf("Enter number >> ");
    scanf("%d", &x);

    int l = ln(x);
    char* s = (char*) malloc(l * sizeof(char));

    process(s, x, l);

    if (strcmp(s, "00000110101000010110110")) {
        printf("Wrong number\n");
    } else {
        printf("donnuCTF{%x}\n", x);
    }

    free(s);
}
```

## Solution