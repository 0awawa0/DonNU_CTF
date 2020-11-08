#include <stdio.h>
#include <string.h>
#include <time.h>


int INPUT_LENGTH = 37;

#define RAND_MAX 32767 

static unsigned long int next = 1;

int rand(void)
{
  next = next * 1103515245 + 12345;
  return (unsigned int)(next/65536) % (RAND_MAX + 1);
}

void srand(unsigned int seed)
{
  next = seed;
}

void shift(char* input, int key) {
	for (int i = 0; i < key; i++) {
		char t = input[0];
		for (int j = 0; j < INPUT_LENGTH - 1; j++) {
			input[j] = input[j + 1];
		}
		input[INPUT_LENGTH - 1] = t;
	}
}

void slice(char* input, int x, int y) {

	char first_slice [x];
	char second_slice [y - x];
	char third_slice [INPUT_LENGTH - y];

	int i = 0;
	for (int j = 0; j < x; first_slice[j] = input[i], j++, i++);
	for (int j = 0; j < (y - x); second_slice[j] = input[i], j++, i++);
	for (int j = 0; j < (INPUT_LENGTH - y); third_slice[j] = input[i], j++, i++);
 
	i = 0;
	for (int j = 0; j < (INPUT_LENGTH - y); input[i] = third_slice[j], j++, i++);
	for (int j = 0; j < x; input[i] = first_slice[j], j++, i++);
	for (int j = 0; j < (y - x); input[i] = second_slice[j], j++, i++);
}

int main(int argc, char const *argv[])
{
	// donnuCTF{sh1ft_it_sl1c3_it_gu3ss_1t}
	char check [] = {-64, -112, 32, 32, 48, 80, -64, -96, -48, 80, -128, 112, -96, -64, -112, -16, -64, -112, 80, 64, 112, 80, 80, -112, -16, -64, -112, 16, 48, 80, 80, 80, -112, 112, -64, -80, 0};
	char input[INPUT_LENGTH];

	printf("Enter the flag >> ");
	fgets(input, INPUT_LENGTH, stdin);

	shift(input, 5);
	slice(input, 5, 10);
	shift(input, 22);

	srand((long) input[0]);
	int key = rand() % 251;

	for (int i = 0; i < INPUT_LENGTH; i++) {
		input[i] = input[i] * key;
	}

	for (int i = 0; i < INPUT_LENGTH; i++) {
		if (input[i] != check[i]) {
			printf("%d != %d. Wrong flag!\n", input[i], check[i]);
			return 0;
		}
	}

	printf("True flag!\n");
	return 0;
}