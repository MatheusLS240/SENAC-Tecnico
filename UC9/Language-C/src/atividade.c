#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int repetirCadastro = 1;

    while (repetirCadastro != 0) {
        system("clear");
        char clienteNome[30];
        char vendedorNome[30];
        char produtoNome[30];
        float produtoPreco = 0;
        int formaPagamentoInt = 0;
        bool formaPagamento = false;
        int quantParcelas = 0;
        float valorParcela = 0;

        printf("Insira o nome do cliente: ");
        fgets(clienteNome, 30, stdin);
        printf("Insira o nome do vendedor: ");
        fgets(vendedorNome, 30, stdin);
        printf("Insira o nome do produto: ");
        fgets(produtoNome, 30, stdin);
        printf("Insira o preço do produto: ");
        scanf("%f", &produtoPreco);
        printf("Insira 1 para pagamento a vista ou 0 para caso contrario: ");
        scanf("%d", &formaPagamentoInt);
        getchar(); 
        formaPagamento = formaPagamentoInt == 1 ? true : false;

        if (formaPagamento) {
            produtoPreco -= (produtoPreco * 0.10); // produtoPreco = produtoPreco - (produtoPreco * 0.10)
        } else {
            produtoPreco += (produtoPreco * 0.15);

            printf("\nQuantas parcelas deseja fazer? (Maximo 12) ");
            scanf("%d", &quantParcelas);
            getchar(); 

            while(quantParcelas > 12) {
                printf("Quantidade de parcelas indisponivel. Tente novamente: (maximo de 12) ");
                scanf("%d", &quantParcelas);
                getchar(); 
            }

            valorParcela = produtoPreco / quantParcelas;
        }

        FILE *arquivo = fopen("../files/cadastroAtividade.txt", "a");

        fprintf(arquivo, "Nome do cliente: %s", clienteNome);
        fprintf(arquivo, "Nome do vendedor: %s", vendedorNome);
        fprintf(arquivo, "Nome do produto: %s", produtoNome);
        fprintf(arquivo, "Preço do produto: %.2f", produtoPreco);
        fprintf(arquivo, "\nForma de pagamento: %s", formaPagamento == 1 ? "A vista" : "Parcelado");
        if(!formaPagamento) {
            fprintf(arquivo, "\nQuantidade de parcelas: %d", quantParcelas);
            fprintf(arquivo, "\nValor da parcela: %.2f", valorParcela);
        }
        fprintf(arquivo, "\n======================================================\n");

        printf("Deseja fazer um novo cadastro? (1 = sim / 0 = não)");
        scanf("%d", &repetirCadastro);
        getchar(); 

        int i;
        for(i = 0; i < 30; i++) {
            clienteNome[i] = '\0';
            vendedorNome[i] = '\0';
            produtoNome[i] = '\0';
        }

        fclose(arquivo);
    }

    return 0;
}