#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char const *argv[])
{
	char* flag = "--REDACTED--";
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