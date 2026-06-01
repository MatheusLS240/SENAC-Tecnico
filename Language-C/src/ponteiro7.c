#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");

    char nomeCompleto[30];
    
    printf("Digite o seu nome completo: \n");
    fgets(nomeCompleto, 30, stdin);
    printf("Olá, Sr.(a) %s\n", nomeCompleto);

    return 0;
}