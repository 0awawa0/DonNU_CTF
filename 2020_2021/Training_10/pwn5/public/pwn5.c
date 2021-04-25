#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FLAG "--REDACTED--"


int checkUser(char* name) {
	int adminToken = 0;
	char nameCopy[64];
	strcpy(nameCopy, name);
	for (int i = 0; i < 64; i++) adminToken *= nameCopy[i];
	if (adminToken == 0xdeadbeef) {
		printf("You are admin. Your flag is: %s\n", FLAG);
	} else {
		printf("You are not admin. Your token is %x\n", adminToken);
	}
}


int main(int argc, char const *argv[])
{	
	char buf[128];
	printf("Enter your name >> ");
	gets(buf);
	checkUser(buf);
	return 0;
}