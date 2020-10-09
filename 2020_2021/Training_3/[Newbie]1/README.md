# 1

## Task

```C
#include <stdio.h>
#include <string.h>


int main(int argc, char const *argv[])
{
	char c [] = {100, 111, 110, 110, 117, 67, 84, 70, 123, 65, 83, 67, 73, 73, 95, 99, 104, 51, 99, 107, 49, 110, 103, 125, 0};
	char s [25];
	printf("Enter the flag >> ");
	fgets(s, 25, stdin);
	if (strcmp(c, s)) {
		printf("Incorrect flag\n");
	} else {
		printf("Correct flag\n");
	}

	return 0;
}
```

## Solution

Just decode numbers as ASCII characters

```Python
>>> n = [100, 111, 110, 110, 117, 67, 84, 70, 123, 65, 83, 67, 73, 73, 95, 99, 104, 51, 99, 107, 49, 110, 103, 125]
>>> "".join(chr(i) for i in n)
'donnuCTF{ASCII_ch3ck1ng}'
```