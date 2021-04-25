#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define FLAG "---REDACTED---"


int main(int argc, char* argv[]){
	
	int isAdmin = 0;
	char buffer[32];
	printf("Enter your name >> ");
	gets(buffer);

	if (isAdmin) {
		printf("You are admin. Here is your flag: %s\n", FLAG);
	} else {
		printf("You are not admin!\n");
	}
	return 0;
}