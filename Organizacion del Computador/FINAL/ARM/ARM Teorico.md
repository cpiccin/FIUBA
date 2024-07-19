# Caso de estudio: ARM

## Características principales 
- Arquitectura Load/Store: la forma de comunicarse con la memoria es solamente a través de Load y Store
- Instrucciones de longitud fija (32 bits) 
- Formatos de instrucciones de 3 direcciones:
    - 2 registros de operacion 
    - 1 registro de resultado
- Ejecución condicional de todas las instrucciones: permite que las instrucciones se ejecuten si se cumplen ciertas instrucciones
- Existen instrucciones de Load-Store de registros múltiples. Si se quiere cargar info de una dirección de memoria se puede hacer de una a varios registros. 


## Organización de los registros 
`R0` a `R12` son registros de proposito general (32 bits)
- Usados por el programador para casi cualquier proposito sin restriccion

`R13` es el Stack Pointer (SP)

`R14` es el Link Register (LR). Se usa para poder volver al flujo principal, se relaciona con poder tener rutinas internas dentro del programa

`R15` es el Program Counter (PC). El RPI en abacus, tiene la direccion de la proxima direccion a ser ejecutada

El *Current Program Status Register* (CPSR) contiene indicadores condicionales y otros bits de estado. No se interactuamos con este registro

![cpsr](https://github.com/user-attachments/assets/90ad0b0b-643d-4e75-9241-dbd0d9265cfe)


## Organizacion de memoria
- Maximo: 2<sup>32</sup> bytes de memoria
- Las **palabras** son de 32 bits
- Existe la **half-word** de 16 bits
- Words están alineadas en posiciones divisibles por 4
- Half-words están alineadas en posiciones pares


## Estructura de un programa
- Forma general de una linea en un modulo de ARM <br>
`label <espacio> opcode <espacio> operandos <espacio> @ comentario`
- Las instrucciones no empiezan en la primer columna, dado que deben estar precedidas por un espacio en blanco, incluso aunque no haya label
- ARM acepta lineas en blanco para mejorar la claridad del codigo

```
    .text                          @ Indica que los siguientes
                                   @ ítems en memoria son
                                   @ instrucciones
start:
    mov r0, #15                    @ Seteo de parámetros:
    mov r1, #20                    @ Se cargan los valores 15 y 20 al registro R0 y R1 respectivamente
    bl func                        @ Llamado a subrutina: se usa branch with link (bl) que bifurca y permite volver al flujo del cual bifurco. Se guarda la direc de la prox instruccion en el LR
    swi 0x11                       @ Fin de programa utilizando Software Interrupt (SWI)
func:                              @ Subrutina
    add r0, r0, r1                 @ r0 = r0 + r1
    mov pc, lr                     @ Retornar desde subrutina: esta guardado en el LR la direc sig al llamado a func, entonces digo que la proxima instruccion (lo que guarda el PC para seguir con el programa) sea lo que esta en el LR
    .end                           @ Marcar fin de archivo
```


## Herramientas: ARMSim#


