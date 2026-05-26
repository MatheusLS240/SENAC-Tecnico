#include <stdio.h>

int main() {
    int ano = 0;

    printf("Digite um ano:");
    scanf("%d", &ano);

    if(ano % 4 == 0) {
        printf("O ano %d é bissexto\n", ano);
    } else {
        printf("O ano %d NÃO é bissexto\n", ano);
    }

    return 0;
}