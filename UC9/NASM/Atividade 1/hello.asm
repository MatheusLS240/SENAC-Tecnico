; ---------------------------------------------------------------------------------;
        ;para executar o código abaixo, usamos os seguintes comandos 
        ;nasm -f elf64 hello.asm -o hello.o -> para gerar o código binario 
        ; ld hello.o -o hello -> para gerar o executável 
        ;./hello -> para executar o arquivo hello
;--------------------------------------------------------------------------;

global _start
    section .text
    _start:                             ;--------------------------------------------------;
        mov rax,1                       ;prepara o sistema para a escrita  
        mov rdi,1                       ;prepara a saida padrão para exibir o resultado  
        mov rsi,message                 ;carrega a mensagem que sera exibida 
        mov rdx,7                       ;quantidades de bytes que sera exibida 
        syscall                         ;chama o sistema para executar os comandos acima 
        mov rax,60                      ;finaliza a chamada do programa acima 
        xor rdi,rdi                     ;limpa a memoria para a proxima execução 
        syscall                         ;chama o sistema para executar os comandos acima
                                        ;---------------------------------------------------;

        section .data
        message:db 'Hello,World',10 



