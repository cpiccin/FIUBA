global main


section .data           
    ocasCapturadas          dw 0; empieza en 0
   
    msgGanoZorro            db "Partida finalizada. Gano el zorro",10,0
    msgGanoOcas             db "Partida finalizada. Ganaron las ocas",10,0

    filePartida             db "partida_guardada.txt",0
    modo                    db "r",0

    format                  db "%s",10, 0
    formatInt               db "%lli", 10, 0

    aux                     dd 0, 0

section .bss
    handlePartida           resq 1
    tablero                 times 50 resb 1 ; tablero 7x7 + null byte 


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
