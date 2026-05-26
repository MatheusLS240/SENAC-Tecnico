#include <stdio.h>

int main() {
    int par = 0;

    printf("Insira um número para saber se é par: ");
    scanf("%d", &par);

    if(par % 2 == 0) {
        printf("O número %d é par\n", par);
    }

    return 0;
}