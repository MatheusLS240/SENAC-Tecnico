#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");

    int i;

    for (i = 0; i < 100; i++) {
        printf("=");
    }
    printf("\nPrograma de Cadastro\n");
    
    char primeiroNome[10];
    char segundoNome[10];
    char email[50];
    int idade;

    printf("Insira seu nome: ");
    fgets(primeiroNome, 10, stdin);
    printf("Insira seu sobrenome: ");
    fgets(segundoNome, 10, stdin);
    printf("Insira seu email: ");
    fgets(email, 50, stdin);
    printf("Insira sua idade: ");
    scanf("%d", &idade);

    FILE *arquivo = fopen("../files/cadastro.txt", "a");
    
    fprintf(arquivo, "Nome: %s", primeiroNome);
    fprintf(arquivo, "Sobrenome: %s", segundoNome);
    fprintf(arquivo, "E-Mail: %s", email);
    fprintf(arquivo, "Idade: %d\n", idade);
    for (i = 0; i < 100; i++) {
        fprintf(arquivo, "=");
    }

    fclose(arquivo);

    return 0;
}