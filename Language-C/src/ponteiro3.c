#include <stdio.h>
#include <stdlib.h>

int main() {
    int idade[6] = {18, 25, 17, 16, 10, 21};
    int *pidade = idade;

    printf("Primeiro elemento é %d\n", idade[0]);
    printf("Primeiro elemento é %d\n", *pidade);
    printf("O endereço do primeiro elemento é %p", pidade);

    pidade++;

    printf("Segundo elemento é %d\n", idade[1]);
    printf("Segundo elemento é %d\n", *pidade);
    printf("O endereço do segundo elemento é %p", pidade);

    pidade++;

    printf("Terceiro elemento é %d\n", idade[2]);
    printf("Terceiro elemento é %d\n", *pidade);
    printf("O endereço do terceiro elemento é %p", pidade);

    pidade++;

    printf("Quarto elemento é %d\n", idade[2]);
    printf("Quarto elemento é %d\n", *pidade);
    printf("O endereço do quarto elemento é %p", pidade);

    pidade++;

    printf("Quinto elemento é %d\n", idade[2]);
    printf("Quinto elemento é %d\n", *pidade);
    printf("O endereço do quinto elemento é %p", pidade);

    pidade++;

    printf("Sexto elemento é %d\n", idade[2]);
    printf("Sexto elemento é %d\n", *pidade);
    printf("O endereço do sexto elemento é %p", pidade);

    return 0;
}