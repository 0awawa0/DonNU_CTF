#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char input[13];
    char str [30] = {121, 65, 53, 112, 71, 115, 127, 97, 100, 102, 69, 64, 68, 117, 111, 113, 86, 118, 59, 48, 57, 43, 38, 104, 111, 101, 106, 54, 71, 115};
    int i,k;
    printf("Enter the flag >> ");
    scanf("%s", input);
    k = 0;
    for ( i = 0; i < 30; i++) {
        if((str[i] % 2 == 0) && (k < 13)) {
            if(str[i] != input[k]) {
            	printf("Wrong flag!\n");
            	return 0;
            }
            k++;
    	}
    }

    printf("Correct flag is donnuCTF{%s}\n", input);
    return 0;
}
