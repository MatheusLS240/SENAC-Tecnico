#include <stdio.h>

int main()
{
    float preco;
    float taxa;
    float parcelas;
    float resultado;
    float resultadoParcelas;

    printf("Digite o preço do produto: ");
    scanf("%f", &preco);

    printf("Digite a taxa de acréscimo sem o simbolo de porcentagem: ");
    scanf("%f", &taxa);

    printf("Digite o número de parcelas: ");
    scanf("%f", &parcelas);

    resultado = preco * (taxa / 100) + preco;
    resultadoParcelas = resultado / parcelas;

    printf("O valor final do produto é R$ %.2f\n", resultado);
    printf("O valor da parcela é R$ %.2f\n", resultadoParcelas);

    return 0;
}