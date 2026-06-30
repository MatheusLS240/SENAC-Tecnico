#include <stdio.h>

int main(){
    int i, num, res;

    printf("Digite um número para fazer a tabuada\n");
    scanf("%d", &num);

    i = 0;
    while(i <= 10){
        res = num * i;
        printf("%d X %d = %d\n",num,i,res);
        i++;

    } 

    return 0;
}

