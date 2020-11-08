#include <stdio.h>



int main() {
    int x ;

    char s [48];
    int d=0;

    char c [] = {121,97,100,101,99,102,113,120,95,83,84,92,105,91,89,108,85,68,79,67,73,94,85,84,67,11,99,115,121,67,85,88,104,124,127,80,85,90,92,111,110,117,100,98,86,108,87,107,0};
	int i;
	for ( i = 0; i <48; i++) {
		if ( c[i]%2==0) {
                s[i]=48;
                d+=2;}
        else{s[i]=49;
        d+=5;}
	}
printf("Enter the number >> ");
	scanf("%d", &x);
	if ( d==x ){
            if( strcmp(s, "110110101100111010111010111111100010100101000011")) {
        printf("Your flag is donnuCTF{0x%x}\n", x);
    } else {
        printf("Wrong!\n");
    }
    }
    else{printf("Wrong!\n");}

   return 0;
}
