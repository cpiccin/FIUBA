global main

extern fopen
extern fclose
extern fgets 
extern printf
extern atoi

section .data           
    ocasCapturadas          dw 0; empieza en 0
   
    msgGanoZorro            db "Partida finalizada. Gano el zorro",10,0
    msgGanoOcas             db "Partida finalizada. Ganaron las ocas",10,0

    filePartida             db "partida_guardada.txt",0
    modo                    db "r",0

    format                  db "%s",0
    formatInt               db "%lli", 0

section .bss
    handlePartida           resq 1
    tablero                 times 50 resb 1 ; tablero 7x7 + null byte 

    cantMovArr              resd 1
    cantMovAbj              resd 1
    cantMovIzq              resd 1
    cantMovDer              resd 1
    cantMovDiagIzqArr       resd 1
    cantMovDiagIzqAbj       resd 1
    cantMovDiagDerArr       resd 1
    cantMovDiagDerAbj       resd 1

    turnoDe                 resb 2 ; turno actual

section .text
main: 
    call manejoDeArchivo 
    sub rsp, 8

    mov rdi, format 
    mov rsi, tablero
    call printf

    mov rdi, format 
    mov rsi, turnoDe
    call printf

    mov rdi, formatInt
    mov rsi, cantMovArr
    call printf 
    ; mov rdi, format
    ; mov rsi, cantMovAbj
    ; call printf    
    ; mov rdi, format
    ; mov rsi, cantMovIzq
    ; call printf    
    ; mov rdi, format
    ; mov rsi, cantMovDer
    ; call printf    
    ; mov rdi, format
    ; mov rsi, cantMovDiagIzqArr
    ; call printf    
    ; mov rdi, format
    ; mov rsi, cantMovDiagIzqAbj
    ; call printf    
    ; mov rdi, format
    ; mov rsi, cantMovDiagDerArr
    ; call printf
    ; mov rdi, format
    ; mov rsi, cantMovDiagDerAbj
    ; call printf


    add rsp, 8

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

    ;leo estadisticas
    mov rdi, r8
    mov rsi, 200
    mov rdx, [handlePartida]
    call fgets
    mov rdi, r8
    call atoi
    mov [cantMovArr], rax
    ; mov rdi, cantMovAbj
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovIzq
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovDer
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovDiagIzqArr
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovDiagIzqAbj
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovDiagDerArr
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets
    ; mov rdi, cantMovDiagDerAbj
    ; mov rsi, 200
    ; mov rdx, [handlePartida]
    ; call fgets



    mov rdi,[handlePartida]
    call fclose 
    add rsp, 8
    
    ret
