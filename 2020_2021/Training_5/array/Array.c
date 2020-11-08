#include <stdio.h>
#include <stdlib.h>
int main() {
    int b[6];
    int i,j,k,tmp;
    int a[6] = {34,123,56,128,67,25};

    for(i = 0 ; i < 5; i++) {
       for(j = 5 ; j >i; j--) {
           if(a[j-1] > a[j]) {
              tmp = a[j-1];
              a[j-1] = a[j] ;
              a[j] = tmp;
           }
        }
    }

printf("Enter the number >> ");

for (i=0; i<6; i++) {
     scanf("%d", &b[i]);
}
printf("Your flag is donnuCTF{");

    for (k=0; k<6;k++){
            if(a[k]==b[k]){
       printf("%d", b[k]);
     }
     else{
      printf("Wrong!");
     }
    }
     printf("}");
  return 0;

}

