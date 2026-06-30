#include <stdio.h>
#include <stdlib.h>

int main() {
    float num1 = 0, num2 = 0, num3 = 0, num4 = 0;

    system("clear");

    printf("Insira a primeira nota");
    scanf("%f", &num1);
    printf("Insira a segunda nota");
    scanf("%f", &num2);
    printf("Insira a terceiro nota");
    scanf("%f", &num3);
    printf("Insira a quarta nota");
    scanf("%f", &num4);

    float media = (num1 + num2 + num3 + num4) / 4;

    system("clear");

    if (media >= 7) {
        printf("\nAprovado!\n");
    } else {
        printf("\nReprovado!\n");
    }

    printf("\n##################################\n");
    printf("Endereço da memória da variavel num1: %p \n", &num1);
    printf("Endereço da memória da variavel num2: %p \n", &num2);
    printf("Endereço da memória da variavel num3: %p \n", &num3);
    printf("Endereço da memória da variavel num4: %p \n", &num4);
    printf("Endereço da memória da variavel media: %p \n", &media);

    return 0;
}