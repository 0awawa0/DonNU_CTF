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

So here we are asked to enter a number. After that our number is passed to function `ln`:

```C
int ln(int x) {

    int t = x;
    int l = 0;

    while (t) {
        t = t >> 1;
        l++;
    }

    return l;
}
```
This function just calculates and returns bit length of our number. Next, the programm dinamicaly allocates memory for an array of chars of size equals to bit length of our input. Later this array, our input and it's bit length are passed to the function `process`:

```C
void process(char* s, int x, int l) {

    int i = l - 1;
    int t = x;

    for (int i = l - 1; t; i--, t = t >> 1) {
        *(s + i) = (char)(49 ^ (t & 1));
    }
}
```

So this function populates newly created array with data. The data is calculated as follows: `(char) (49 ^ (t & 1))`. Number 49 is xored with least significant bit of our input. This operation will return `48` if it is `1` adn `49` if it is `0`.  `48` and `49` are just ASCII codes for `0` and `1`. That means if least significant bit of the number we input is `0`, character `1` will be added to the string. Other way character `0` will be added. So `process` function just write inverted binary code of the input number.

In the end if this code equals to `00000110101000010110110` we get the flag. Now it is obvious, that we must input `0b11111001010111101001001 = 8171337`:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents</b></font>$ ./6
Enter number &gt;&gt; 8171337
donnuCTF{7caf49}
<font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents</b></font>$ </pre>