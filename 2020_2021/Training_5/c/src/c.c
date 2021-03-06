#include <stdio.h>
#include <stdlib.h>


int length(char* s) {
    int i = 0;
    while(s[i]) i++;
    return i;
}

short change_sample(unsigned char lower_byte, unsigned char upper_byte, char lower_flag_byte, char upper_flag_byte) {
    unsigned char changed_lower_byte = lower_byte;
    changed_lower_byte &= ~1;
    changed_lower_byte = changed_lower_byte | (49 - lower_flag_byte);

    unsigned char changed_upper_byte = upper_byte;
    changed_upper_byte &= ~1;
    changed_upper_byte = changed_upper_byte | (49 - upper_flag_byte);
    return (changed_lower_byte << 8) | changed_upper_byte;
}

void process(FILE* input_file, FILE* output_file, char* flag, int flag_length) {

    unsigned char t;
    for (int i = 0; i < 4; i++) {
        fread(&t, 1, 1, input_file);
        fwrite(&t, 1, 1, output_file);
    }

    int chunk_size = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    chunk_size = chunk_size | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    chunk_size = (t << 8) | chunk_size;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    chunk_size = (t << 16) | chunk_size;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    chunk_size = (t << 24) | chunk_size;

    for (int i = 0; i < 8; i++) {
        fread(&t, 1, 1, input_file);
        fwrite(&t, 1, 1, output_file);
    }

    int subchunk_size = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    subchunk_size = subchunk_size | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    subchunk_size = subchunk_size | (t << 8);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    subchunk_size = subchunk_size | (t << 16);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    subchunk_size = subchunk_size | (t << 24);

    short audio_format = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    audio_format = audio_format | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    audio_format = audio_format | (t << 8);

    short number_of_channels = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    number_of_channels = number_of_channels | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    number_of_channels = number_of_channels | (t << 8);

    int sample_rate = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    sample_rate = sample_rate | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    sample_rate = sample_rate | (t << 8);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    sample_rate = sample_rate | (t << 16);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    sample_rate = sample_rate | (t << 24);

    int byte_rate = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    byte_rate = byte_rate | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    byte_rate = byte_rate | (t << 8);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    byte_rate = byte_rate | (t << 16);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    byte_rate = byte_rate | (t << 24);

    short block_align = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    block_align = block_align | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    block_align = block_align | (t << 8);

    short bits_per_sample = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    bits_per_sample = bits_per_sample | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    bits_per_sample = bits_per_sample | (t << 8);

    for (int i = 0; i < 4; i++) {
        fread(&t, 1, 1, input_file);
        fwrite(&t, 1, 1, output_file);
    }

    int data_length = 0;
    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    data_length = data_length | t;

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    data_length = data_length | (t << 8);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    data_length = data_length | (t << 16);

    fread(&t, 1, 1, input_file);
    fwrite(&t, 1, 1, output_file);
    data_length = data_length | (t << 24);

    unsigned char lower_byte;
    unsigned char upper_byte;
    for (int i = 0; i < data_length; i += 2) {
        fread(&lower_byte, 1, 1, input_file);
        fread(&upper_byte, 1, 1, input_file);
        unsigned char lower_flag_byte = flag[i % flag_length];
        unsigned char upper_flag_byte = flag[(i + 1) % flag_length];
        short new_sample = change_sample(lower_byte, upper_byte, lower_flag_byte, upper_flag_byte);
        lower_byte = new_sample & 0xff;
        upper_byte = (new_sample >> 8) & 0xff;
        fwrite(&lower_byte, 1, 1, output_file);
        fwrite(&upper_byte, 1, 1, output_file);
    }

    while(fread(&t, 1, 1, input_file)) {
        fwrite(&t, 1, 1, output_file);
    }
}

int main(int argc, char const *argv[]) {

    FILE* input = fopen("input", "rb");
    FILE* output = fopen("output", "wb");

    // donnuCTF{chang1ng_th3_wav3}
    // 011001000110111101101110011011100111010101000011010101000100011001111011011000110110100001100001011011100110011100110001011011100110011101011111011101000110100000110011010111110111011101100001011101100011001101111101
    char flag [217];
    printf("Enter the flag >> ");
    fgets(flag, 217, stdin);

    process(input, output, flag, length(flag));

    fclose(input);
    fclose(output);
}