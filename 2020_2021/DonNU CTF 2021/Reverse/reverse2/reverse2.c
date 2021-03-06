#include <stdio.h>


int l(char *s) {
	int i = 0;
	while (s[i]) i++;
	return i;
}

void process(char* s) {
	int k = l(s);
	for (int i = 0; i < k; i++) {
		s[i] = (char)(k + s[i]);
	}
}

int main(int argc, char const *argv[]) {

	char s [100];

	printf("Input >> ");
	fgets(s, 100, stdin);
	process(s);
	printf("Output >> ");
	for (int i = 0; s[i]; i++) printf("%02hhx", s[i]);
	printf("\n");
	return 0;
}

