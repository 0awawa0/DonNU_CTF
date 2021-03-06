#include <stdio.h>
#include <stdlib.h>


unsigned char code(unsigned char x) {
    return x ^ (x >> 1);
}

void encrypt(FILE* input, FILE* output) {
    unsigned char t;
    while (fread(&t, 1, 1, input)) {
        t = code(t);
        fwrite(&t, 1, 1, output);
    }
}

int main(int argc, char const *argv []) {

    FILE* input_file = fopen("input", "rb");
    FILE* output_file = fopen("output", "wb");
    encrypt(input_file, output_file);
    fclose(input_file);
    fclose(output_file);
}