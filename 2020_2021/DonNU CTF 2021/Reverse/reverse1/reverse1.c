#include <stdio.h>


int checkArr [] = {399, 444, 439, 439, 468, 268, 335, 279, 492, 407, 468, 439, 380, 436, 388, 220, 415, 500, 39};

int check(char* s) {
	int result = 0;
	for (int i = 0; s[i]; i++)
		if (s[i] % 2) result += checkArr[i] - (s[i] * 4);
		else result += checkArr[i] - (s[i] * 4 - 1);
	return result;
}

int main(int argc, char const *argv[]) {
	char s [100];
	printf("Enter the flag >> ");
	fgets(s, 100, stdin);

	if (check(s)) {
		printf("Wrong flag!\n");
	} else {
		printf("That is correct!\n");
	}

	return 0;
}