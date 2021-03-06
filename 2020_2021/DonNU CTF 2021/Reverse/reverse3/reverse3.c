#include <stdio.h>


char l(char* s) {
	int i = 0;
	while (s[i]) i++;
	return i;
}

char p(char *s) {
	char i = 0;
	char res = 0;
	while (s[i]) {
		res += s[i];
		i++;
	}

	if (res < 0) res = -res;
	return res;
}

void process(char* s) {
	char k = p(s) % 251;
	int ls = l(s);
	for (int i = 0; i < ls; i++) s[i] = (char)((k * s[i]) % 251);
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
