# 4

## Task

```C
#include <stdio.h>


int l(char* s) {
	int i;
	for (i = 0; s[i]; i++);
	return i;
}


int check(char* s) {
	int d = 0;
	char check [] = {100, 11, -1, 0, 7, -50, 17, -14, 53, -18, 11, -1, -20, 2, -48, 0, 46, 2, 1, -50, 69, -62, 40, 5, 5, -3, 0, -51, 63, -63, 59, -11, -48, 74, -115};
	for (int i = 0; i < l(s); i++) {
		if (s[i] - d != check[i]) {
			return 0;
		}
		d = s[i];
	}
	return 1;
}


int main(int argc, char const *argv[])
{
	char s[100];
	printf("Enter the flag >> ");
	fgets(s, 100, stdin);
	if (check(s)) {
		printf("Flag is correct!\n");
	} else {
		printf("Flag is incorrect!\n");
	}

	return 0;
}
```

## Solution

In this task we need to input some flag to check. The flag is checked in the following loop:

```C
for (int i = 0; i < l(s); i++) {
	if (s[i] - d != check[i]) {
		return 0;
	}
	d = s[i];
}
```

First of all, there is some function `l` calculated over our input:

```C
int l(char* s) {
	int i;
	for (i = 0; s[i]; i++);
	return i;
}
```

Here we can see that the loop will stop when `s[i]` is `0` and that will happend only when it will reach the end of the string. So function will return `i` which is equals to the length of our input.

Now back to the `check` function. We can see that if `s[i] - d` not equals to `check[i]`, where `d` equals `0` for the first iteration and `s[i-1]` for others, the function will return `0`. Although we need it to return `1`.

So we can declare that `s[i] = check[i] + s[i - 1]` and `s[0] = check[0] = 100`. Having that it is pretty easy to calculate the flag:

```Python
>>> check = [100, 11, -1, 0, 7, -50, 17, -14, 53, -18, 11, -1, -20, 2, -48, 0, 46, 2, 1, -50, 69, -62, 40, 5, 5, -3, 0, -51, 63, -63, 59, -11, -48, 74, -115]
>>> s = [100]
>>> for i in range(1, len(check)):
...     s.append(s[i - 1] + check[i])
... 
>>> s
[100, 111, 110, 110, 117, 67, 84, 70, 123, 105, 116, 115, 95, 97, 49, 49, 95, 97, 98, 48, 117, 55, 95, 100, 105, 102, 102, 51, 114, 51, 110, 99, 51, 125, 10]
>>> "".join(chr(i) for i in s)
'donnuCTF{its_a11_ab0u7_diff3r3nc3}\n'

```