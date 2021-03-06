# 2

## Task

```C
#include <stdio.h>


int check(int x) {
	int a = x * x;
	int b = a - 2315 * x;
	int c = b - 12813995;
	return c;
}


int main(int argc, char const *argv[])
{
	int x;
	printf("Enter the number >> ");
	scanf("%d", &x);
	if (check(x) == -x) { 
		printf("Flag is: donnuCTF{0x%x}\n", x);
	} else {
		printf("Incorrect number\n");
	}
	return 0;
}
```

## Solution

That's just an equation to be solved. `x` must be such number that:
![equation](http://www.sciweavers.org/tex2img.php?eq=x%5E%7B2%7D%20-%202314%20%2A%20x%20-%2012813995%20%3D%200&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

Solving this we have two numbers to test as a flag:
```
x1 = 4919
x2 = -2605
```