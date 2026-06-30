#include <stdio.h>

int main() {
   int num1;
   int num2;
   int soma;
   int multiplicacao;
   int divisao;
   int subtracao;

   printf("Digite um numero inteiro menino inteligente:\n\n");
   scanf("%d", &num1);

   printf("Digite outro numero inteiro\n\n");
   scanf("%d", &num2);

   soma = num1 + num2;
   multiplicacao = num1 * num2;
   divisao = num1 / num2;
   subtracao = num1 - num2;

   printf("A soma dos numeros %d e %d resultou em %d\n", num1, num2, soma);
   printf("A multiplição dos numeros %d e %d resultou em %d\n", num1, num2, multiplicacao);
   printf("A divisão dos numeros %d e %d resultou em %d\n", num1, num2, divisao);
   printf("A subtração dos numeros %d e %d resultou em %d\n", num1, num2, subtracao);

   return 0;
}