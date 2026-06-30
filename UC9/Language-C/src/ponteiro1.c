#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 35;
    int *ptrA = &a;

    printf("O valor da variavel A é %d\n", a);
    printf("O endereço de memoria da variavel A é %p\n", ptrA);
    printf("O valor que está no endereço da variavel A é %d\n", *ptrA);

    return 0;
}