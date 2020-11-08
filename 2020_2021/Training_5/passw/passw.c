#include <stdio.h>


int l(char* s) {
	int i;
	for (i = 0; s[i]; i++);
	return i;
}


int check(char* s) {
    int i;
	char c [] = {100,50,54,57,99,101,49,53,102,57,99,52,52,98,99,51,57,57,50,97,53,102,52,101,53,102,50,55,51,101,48,54};
	for ( i = 0; i < l(s); i++) {
		if (s[i] == c[i]) {
			return 1;
		}
	}
	return 0;
}


int main(int argc, char const *argv[])
{
	char s[100];
	printf("Enter the flag >> ");
	fgets(s, 100, stdin);
	if (check(s)) {
		   printf("Flag is  like this, but not exaxtly: donnuCTF{%s}", s);
	} else {
		printf("Wrong flag!\n");
	}

	return 0;
}

