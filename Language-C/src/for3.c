#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");

    int base = 0;
    int potencia = 0;
    int res = 1;

    printf("Insira o numero da base: ");
    scanf("%d", &base);

    printf("Insira o numero da potencia: ");
    scanf("%d", &potencia);

    for(int i = 1; i <= potencia; i++) {
        res *= base;
    }
    
    printf("O resultado da conta é %d\n", res);

    return 0;
}
