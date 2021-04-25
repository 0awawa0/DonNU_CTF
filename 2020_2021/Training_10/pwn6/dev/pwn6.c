#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char const *argv[])
{
	char* flag = "donnuCTF{9f1ca67b2462ea7f20e012622f09cab2}";
	char check [128];
	printf("Enter the flag >> ");
	gets(check);
	if (!strcmp(check, flag)) {
		printf("Your flag is correct!\n");
	} else {
		printf(check);
		printf(" is not a flag!\n");
	}

	return 0;
}