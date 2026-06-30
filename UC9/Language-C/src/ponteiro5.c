#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");

    char primeiroNome[10];
    
    printf("Digite o seu nome: \n");
    scanf("%s\n", primeiroNome);
    printf("Ola, Sr(a). %s\n", primeiroNome);

    return 0;
}