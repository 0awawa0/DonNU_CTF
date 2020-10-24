#include <stdio.h>


int main(int argc, char const *argv[]) {

    printf("Enter the flag >> ");
    char input [43];
    fgets(input, 43, stdin);

    if (
        input[0] == 'd' 
        && input[1] == 'o'
        && input[2] == 'n'
        && input[3] == 'n'
        && input[4] == 'u'
        && input[5] == 'C'
        && input[6] == 'T'
        && input[7] == 'F'
        && input[8] == '{'
        && input[9] == 'n'
        && input[10] == 'u'
        && input[11] == 'm'
        && input[12] == 'b'
        && input[13] == '3'
        && input[14] == 'r'
        && input[15] == 's'
        && input[16] == '_'
        && input[17] == 'o'
        && input[18] == 'r'
        && input[19] == '_'
        && input[20] == 'c'
        && input[21] == 'h'
        && input[22] == 'a'
        && input[23] == 'r'
        && input[24] == 'a'
        && input[25] == 'c'
        && input[26] == 't'
        && input[27] == 'e'
        && input[28] == 'r'
        && input[29] == 's'
        && input[30] == '?'
        && input[31] == '_'
        && input[32] == 'w'
        && input[33] == 'h'
        && input[34] == 'a'
        && input[35] == 't'
        && input[36] == '3'
        && input[37] == 'v'
        && input[38] == '3'
        && input[39] == 'r'
        && input[40] == '}'
    ) {
        printf("Flag is correct\n");
        return 0;
    }

    printf("Flag is incorrect\n");
    return 1;
}