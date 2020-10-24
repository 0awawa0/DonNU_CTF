#include <stdio.h>
#include <stdlib.h>


char gf(int a, int b) {
    int t;
    int at = a;
    int bt = b;

    while (bt) {
        t = at % bt;
        at = bt;
        bt = t;
    }

    return (char) at;
}

void encrypt(FILE* input, FILE* output) {
    fseek(input, 0L, SEEK_END);
    int size = ftell(input);
    rewind(input);

    char t = 0;
    for (int i = 0, j = 3; i < size; i++, j++) {
        fread(&t, 1, 1, input);
        while (gf(j, 256) != 1) { j++; }
        t = (t * j) % 256;
        fwrite(&t, 1, 1, output);
    }
}

int main(int argc, char const *argv[]) {
    FILE *input_file = fopen("input", "rb");
    FILE *output_file = fopen("output", "wb");

    if (input_file == NULL) {
        printf("Error! Can't open file\n");
        exit(-1);
    }

    encrypt(input_file, output_file);

    fclose(input_file);
    fclose(output_file);
}