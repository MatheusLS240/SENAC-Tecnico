#include <stdio.h>

int main(){
    int linha = 1, coluna = 1;


    while(linha <= 5 ){
        while(coluna <= linha ){
            printf("#");
            coluna++;
        }
        
        coluna = 1;   
        printf("\n");
        linha++;
    }
}