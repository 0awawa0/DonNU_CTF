#include <stdio.h>
#include <stdlib.h>

#define FLAG "--REDACTED--"

void checkUser(int token) {

	char buffer[23];
	printf("Enter your username >> ");
	gets(buffer);
	if (token == 0xdeadbeef) {
		printf("Your flag is %s\n", FLAG);
	} else {
		printf("No flag for you.\n");
	}
}


int main(int argc, char const *argv[])
{
	
	checkUser(0x556321);
	return 0;
}