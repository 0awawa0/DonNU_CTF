#include <stdio.h>


int check(int x) {
	int a = 1231;
	for (int i = 0; i < x; i++, a--);
	return a + 1231;
}


int main(int argc, char const *argv[])
{
	int x;
	printf("Enter the secret number >> ");
	scanf("%d", &x);
	if (!check(x)) {
		printf("Flag is donnuCTF{0x%x}\n", -x);
	} else {
		printf("Incorrect number\n");
	}
	return 0;
}
