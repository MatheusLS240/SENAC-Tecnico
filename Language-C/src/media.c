#include <stdio.h>

int main() {
    float num1 = 0, num2 = 0, num3 = 0, num4 = 0;

    printf("Insira a primeira nota");
    scanf("%f", &num1);
    printf("Insira a segunda nota");
    scanf("%f", &num2);
    printf("Insira a terceiro nota");
    scanf("%f", &num3);
    printf("Insira a quarta nota");
    scanf("%f", &num4);

    float media = (num1 + num2 + num3 + num4) / 4;

    if (media >= 7) {
        printf("Aprovado!");
    } else {
        printf("Reprovado!");
    }
}