#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void printFlag() {
	char buf[64];
	FILE* f = fopen("./flag", "r");
	fgets(buf, sizeof(buf), f);
	printf("%s\n", buf);
}


void checkFlag() {
	char buf[64];
	FILE* f = fopen("./flag", "r");
	fgets(buf, sizeof(buf), f);

	char flag[64];
	printf("Enter the flag >> ");
	gets(flag);
	if (!strcmp(buf, flag)) {
		printf("Flag is correct!\n");
	} else {
		printf("Flag is incorrect!\n");
	}
}


int main(int argc, char const *argv[])
{

	checkFlag();
	return 0;
}