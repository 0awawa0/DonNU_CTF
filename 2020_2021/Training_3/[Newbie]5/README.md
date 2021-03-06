# 5

## Task

```C
#include <stdio.h>


int process(char* a, char* b, char* c, char* d) {

    return *a | (*b << 8) | (*c << 16) | (*d << 24);
}


int main(int argc, char const *argv[]) {

    char a, b, c, d;

    printf("Enter 4 characters >> ");
    scanf("%c", &a);
    scanf("%c", &b);
    scanf("%c", &c);
    scanf("%c", &d);

    if (process(&a, &b, &c, &d) == 1815097443) {
        printf("Flag is: donnuCTF{%d%d%d%d}\n", a, b, c, d);
        return 0;
    }

    printf("No flag for you\n");
    return 1;
}
```

## Solution

We are asked to input for characters. After that the function `process` just converts this four bytes to a single 4-byte integer. And if it will return `1815097443` the programm will print the flag.

So we just need to convert this number back to bytes:

```Python
>>> n = 1815097443
>>> n.to_bytes(4, "little")
b'c00l'
```

And feeding these characters to the program will give us some the flag:
<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>/media/awawa/01D5A880EB50D0C0/CTF/2020_2021/Тренировка 3/Tasks</b></font>$ ./5
Enter 4 characters &gt;&gt; c00l
Flag is: donnuCTF{994848108}
</pre>