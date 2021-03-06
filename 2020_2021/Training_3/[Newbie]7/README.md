# 7

## Task

```C
#include <stdio.h>

char s [] = {48, 49, 50, 0, 50, 49, 100, 121, 0, 89, 50, 67, 62, 61, 64, 0, 100, 111, 0, 58, 103, 58, 60, 87, 93, 115, 121, 0, 100, 111, 110, 110, 117, 67, 84, 70, 123, 119, 97, 55, 99, 104, 95, 116, 104, 51, 95, 110, 117, 108, 108, 95, 98, 121, 116, 51, 125, 0, 123, 55, 77, 0};


int main(int argc, char const *argv[]) {
    int x;

    printf("Enter number >> ");
    scanf("%d", &x);
    printf("Your flag is: %s\n",  s + x);    
}
```

## Solution

This one is easy. The programm asks us to input number `x`. After that it prints the string from the array `s` starting from `x` index. Clearly, we need to find an offset of the flag within the array. Knowing, that the flag starts witn `100, 111, 110` we find the offset `28`:

<pre><font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents</b></font>$ ./7
Enter number &gt;&gt; 28
Your flag is: donnuCTF{wa7ch_th3_null_byt3}
<font color="#4E9A06"><b>awawa@awawa-pc</b></font>:<font color="#3465A4"><b>~/Documents</b></font>$</pre>