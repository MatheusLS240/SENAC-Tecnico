#include <stdio.h>
#include "../lib/funclayout.h"
#include "../lib/funcsoma.h"

int main() {
    int x = 0, y = 0, z = 0;

    cabecalho();

    printf("Digite um número inteiro: ");
    scanf("%d", &x);
    printf("Digite um outro número inteiro: ");
    scanf("%d", &y);

    z = soma(x, y);

    rodape();

    return 0;
}
