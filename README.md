# Estudo da linguagem C e NASM
## Aplicada a lógica de programação e algoritimo

<p align="center">
    <img src="logo.jpg" width="300" height="300">
</p>

---

Estudos das principais estruturadas da linguagem de programação C.

Vamos listar os itens trabalhados neste repositório
    
    * Variáveis
    * Comandos de Entrada e Saída(IO-Input output):
        * printf
        * scanf
    * Desvio de fluxo Simples (if ... )1
    * Desvio de fluxo Multiplo (if ... else ...)
    * Estrutura de Repetição While(Enquanto)
    * Estrutura de Repetição For(Para)
    * Função (Módulos)
        - Função Interna (Dentro do arquivo .c)
        - Função Externa (Dentro do arquivo .h)
    * Importação de Módulos
        - Módulos da linguagem (stdio.h)
        - Módulos do usuário (funcoes.h)
    * Ponteiro
    * Criação de arquivos

#### Demonstração de uma estrutura simples de arquivo .c

``` c
#include <stdio.h>

int main() {
    int x = 10;
    
    printf("O valor é %d\n", x)
    
    return 0;
}