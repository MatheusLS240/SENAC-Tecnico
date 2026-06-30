section .data
    num1 dq 10          				; 'dq' (define quad-word) aloca 64 bits para o número
    num2 dq 20

section .bss
    res resb 20         				; Reservamos 20 bytes (suficiente para números grandes de 64 bits) Caso faça cálculos com números maiores

global _start

section .text
_start:
							; 1. Soma os valores (usando registradores de 64 bits)
    mov rax, [rel num1]
    mov rbx, [rel num2]
    add rax, rbx

							; 2. Prepara a conversão de Inteiro para ASCII (String)


    mov rcx, res        				; rcx aponta para o início do buffer
    add rcx, 19         				; move rcx para o final do buffer
    mov byte [rcx], 0xA 				; coloca um "Enter" (\n) no final
    mov rbx, 10         				; base 10 para a divisão

convert_loop:
    dec rcx             				; move o ponteiro um byte para trás
    xor rdx, rdx        				; zera rdx (necessário antes do comando div)
    div rbx             				; divide RAX por 10 (Quociente vai para RAX, Resto para RDX)
    add dl, '0'         				; soma 48 (código ASCII do '0') para converter o resto em caractere
    mov [rcx], dl       				; guarda o caractere no buffer
    test rax, rax       				; verifica se o quociente chegou a zero
    jnz convert_loop    				; se RAX não for zero, repete o processo

    							; 3. Calcula o tamanho da string a ser exibida em tela
    mov rdx, res        
    add rdx, 20         
    sub rdx, rcx        				; subtrai a posição atual do fim (RDX agora contém o tamanho)

							; 4. Chamada de sistema para exibir na tela (sys_write)
    mov rax, 1          				; número da syscall sys_write (1 no x86_64)
    mov rdi, 1          				; descritor de arquivo 1 (stdout)
    mov rsi, rcx        				; rsi recebe o ponteiro para o início da string
    							; rdx já contém o tamanho calculado no passo 3
    syscall             				; chama o kernel (substitui o int 0x80)

							; 5. Encerrar o programa (sys_exit)
    mov rax, 60         				; número da syscall sys_exit (60 no x86_64) para sair da execução e retirar os dados e memória
    xor rdi, rdi        				; código de retorno 0 em rdi, ou seja, limpar o setor de memória 
    syscall             				; chama o kernel( chamada de sistema para a execução dos comandos acima)