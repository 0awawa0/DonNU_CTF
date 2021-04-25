#include <stdio.h>
#include <stdlib.h>


void printFlag() {
	printf("That is a superstring!\n");
	char buf[256];
	FILE* f = fopen("./flag", "r");
	if (f == NULL)
	{
		puts("Something went wrong: flag.txt not found.\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}


int main(int argc, char const *argv[])
{
	int code = 0xfadc84a3;
	char buffer[64];
	printf("Gimme some string >> ");
	gets(buffer);

	if (code == 0xba4332ff) {
		printFlag();
	} else {
		printf("Nice string! Me like it!\n");
	}

	return 0;
}