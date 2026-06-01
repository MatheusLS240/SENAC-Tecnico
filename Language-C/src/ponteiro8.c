#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");

    int i;

    for (i = 0; i < 100; i++) {
        print("=");
    }
    printf("\nPrograma de Cadastro\n");
    
    char primeiroNome[10];
    char segundoNome[10];
    char email[50];
    int idade;

    FILE *arquivo = fopen('files/cadastro.txt', 'w');

    return 0;
}