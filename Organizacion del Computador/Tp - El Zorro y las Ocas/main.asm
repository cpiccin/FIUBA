global main


section .data           

    filePartida             db "partida_guardada.txt",0
    modo                    db "r",0

section .bss
    handlePartida           resq 1
    turnoDe                 resb 2 ; turno actual

section .text
main: 
    call manejoDeArchivo 

    ret

manejoDeArchivo: 
    ; abrir archivo
    sub rsp, 8
    mov rdi, filePartida
    mov rsi, modo 
    call fopen
    mov [handlePartida], rax 

    ;leo tablero  
    mov rdi, tablero
    mov rsi, 200
    mov rdx, [handlePartida]
    call fgets 

    ;leo turnoDe
    mov rdi, turnoDe
    mov rsi, 200
    mov rdx, [handlePartida]
    call fgets 

    mov rdi,[handlePartida]
    call fclose 
    add rsp, 8
    
    ret
