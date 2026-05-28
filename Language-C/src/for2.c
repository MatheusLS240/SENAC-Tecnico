#include <stdio.h>
#include <stdlib.h>

int main() {
    system("clear");
    
    int ano, contador = 0;

    for(ano = 1950; ano <= 2026; ano++) {
        if(ano % 4 == 0) {
            printf("O ano %d é bissexto\n", ano);
            contador++;
        }
    }

    printf("\nExiste %d anos bissextos entre 1950 e 2026", contador);

    return 0;
}
