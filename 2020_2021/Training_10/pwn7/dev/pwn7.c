#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


char buf[64];

int main(int argc, char **argv) {

	
	printf("Enter your name >> "); 
	fgets(buf, 64, stdin);
	buf[strlen(buf)-1] = '\0';
	
	srand(time(NULL));
	int a = rand() % 1000000;

	printf("Hello, ");
	printf(buf);
	printf(". I am thinking of a random number, guess it and I will give you flag\n");
	printf("Your guess >> ");

	int guess;
	char num[8];
	fgets(num,8,stdin);
	sscanf(num,"%d",&guess);

	if (guess == a){
		printf("That's right, your flag: donnuCTF{109c85c8e712340a94fe4dbb022f0048}\n");
	} else {
		printf("No, my number was %d.\n", a); 
	}
	fflush(stdout);
	return 0;
}