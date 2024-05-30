global main

extern fopen
extern fclose
extern fgets 
extern printf

section .data           
    ocasCapturadas          dw 0; empieza en 0

    prueba                  db "hola",0
    
    msgGanoZorro            db "Partida finalizada. Gano el zorro",10,0
    msgGanoOcas             db "Partida finalizada. Ganaron las ocas",10,0

    filePartida             db "partida_guardada.txt",0
    modo                    db "r",0

    format                  db "%s",0

section .bss
    handlePartida           resq 1
    tablero                 times 50 resb 1 ; tablero 7x7 + null byte 
    estadisticas            times 9 resw 1 ; vector de estadisticas: [arr, abj, izq, der, diagArrIzq, diagArrDer, diagAbjIzq, diagAbjDer]
    turnoDe                 resd 1 ; turno actual

section .text
main: 
    call manejoDeArchivo 



manejoDeArchivo: 
    ; abrir archivo
    mov rdi, filePartida
    mov rsi, modo 
    sub rsp, 8
    call fopen
    add rsp, 8
    mov [handlePartida], rax 

    ;leo tablero  
    mov rdi, tablero
    mov rsi, 50
    mov rdx, [handlePartida]
    sub rsp, 8
    call fgets 
    add rsp, 8
    ; ;leo estadisticas
    ; mov rdi, estadisticas
    ; mov rsi, 8
    ; mov rdx, [handlePartida]
    ; sub rsp, 8
    ; call fgets 
    ; add rsp, 8
    ; ;leo turnoDe
    ; mov rdi, turnoDe
    ; mov rsi, 1
    ; mov rdx, [handlePartida]
    ; sub rsp, 8
    ; call fgets 
    ; add rsp, 8

    mov rdi,[handlePartida]
    sub rsp, 8
    call fclose 
    add rsp, 8
    
    mov rdi, format ; pointer to format string
    mov rsi, tablero ; pointer to string to print
    sub rsp, 8 ; align stack
    call printf
    add rsp, 8 ; restore stack

    ; ; print estadisticas
    ; ; note: this assumes that estadisticas is a null-terminated string
    ; mov rdi, format ; pointer to format string
    ; mov rsi, estadisticas ; pointer to string to print
    ; sub rsp, 8 ; align stack
    ; call printf
    ; add rsp, 8 ; restore stack

    ; ; print turnoDe
    ; ; note: this assumes that turnoDe is a null-terminated string
    ; mov rdi, format ; pointer to format string
    ; mov rsi, turnoDe ; pointer to string to print
    ; sub rsp, 8 ; align stack
    ; call printf
    ; add rsp, 8 ; restore stack
    ret