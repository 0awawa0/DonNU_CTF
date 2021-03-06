#include <stdio.h>
#include <string.h>


int main(int argc, char const *argv[]) {

    printf("Enter the flag >> ");

    char* s = "donnuCTF{yup_just_4_str1ng_ch3ck}";
    char input [34];
    fgets(input, 34, stdin);

    if (!strcmp(s, input)) {
        printf("Flag is correct\n");
    } else {
        printf("Flag is incorrect\n");
    }
    return 0;
}