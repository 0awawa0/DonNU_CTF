# 3

## Task

```C
#include <stdio.h>


int check(int x) {
	int a = 1337;
	for (int i = 0; i < x; i++, a--);
	return a + 1337;
}


int main(int argc, char const *argv[])
{
	int x;
	printf("Enter the number >> ");
	scanf("%d", &x);
	if (!check(x)) {
		printf("Flag is donnuCTF{0x%x}\n", -x);
	} else {
		printf("Incorrect number\n");
	}
	return 0;
}
```

# Solution

Closely looking at the code you can see that function `check` should return `0`. And looking at that function we can see an equation:

![equation1](http://www.sciweavers.org/tex2img.php?eq=1337%20-%20x%20%2B%201337%20%3D%200&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

So `x = 2 * 1337`