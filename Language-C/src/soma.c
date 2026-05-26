#include <stdio.h>

int main() {
   int num1;
   int num2;
   int soma;

   printf("Digite um numero inteiro e aperte enter: \n\n\n");
   scanf("%d", &num1);

   printf("Digite outro numero inteiro: \n\n\n");
   scanf("%d", &num2);

   soma = num1 + num2;

   printf("A soma dos numeros %d e %d resultou em %d\n", num1, num2, soma);
   return 0;
}