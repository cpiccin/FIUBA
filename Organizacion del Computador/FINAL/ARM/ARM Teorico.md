# Caso de estudio: ARM

## ARM - Arquitectura
ARM está basado en una arquitectura load/store, reduciendo así el set de instrucciones; esto significa que el núcleo no puede operar directamente con la memoria. Todas las operaciones de datos deben realizarse mediante registros.

### Organizacion de memoria
- Maximo: 2<sup>32</sup> bytes de memoria
- Las **palabras** son de 32 bits
- Existe la **half-word** de 16 bits
- Words están alineadas en posiciones divisibles por 4
- Half-words están alineadas en posiciones pares

### Set de registros
`R0` a `R12` son registros de proposito general (32 bits)
- Usados por el programador para casi cualquier proposito sin restriccion

`R13` es el Stack Pointer (SP)

`R14` es el Link Register (LR). Se usa para poder volver al flujo principal, se relaciona con poder tener rutinas internas dentro del programa: es usado como registro enlace a subrutinas (LR) y almacena la dirección de retorno cuando una se realiza una operación *Branch with Link*, la cual se calcula desde el registro PC. Siendo así, para volver desde una subrutina puede ejecutarse: `MOV r15, r14` o `MOV pc, lr`.

`R15` es el Program Counter (PC). El RPI en abacus, tiene la direccion de la proxima direccion a ser ejecutada. Como todas las instrucciones tienen longitud de 32 bits y deben estar alineadas a word (cada word es de 4 bytes, esto significa que cada instrucción comienza en una posición de memoria divisible por 4), el valor almacenado en el registro Contador del Programa (PC) es almacenado en los bits [31:2] con los bits [1:0].

El *Current Program Status Register* (CPSR) contiene indicadores condicionales y otros bits de estado. No se interactuamos con este registro

![cpsr](https://github.com/user-attachments/assets/90ad0b0b-643d-4e75-9241-dbd0d9265cfe)

### Sintaxis
- Las etiquetas pueden definirse utilizando una secuencia de caracteres alfanuméricos, barras inferiores (_) y puntos (.) que no comienzan con un número.
- Los códigos de operación son palabras reservadas que no pueden ser utilizados como identificadores válidos.
- Las cadenas de caracteres (strings) deben ir entre comillas dobles (") y los caracteres especiales siguen la convención de C:
```
    newline \n
    tab \t
    quote \"
```
- La presencia del caracter @ en una línea indica el comienzo de un comentario que se extiende hasta el final de la línea.
- El caracter ; puede ser usado en lugar de una nueva línea para separar sentencias.
- Tanto # como $ pueden ser usados para indicar operandos inmediatos.

### Directivas
| Directiva            | Comportamiento | 
|----------------------|----------------|
|`.equ sym, constant`| Da el nombre simbólico *sym* a una constante *constant*.|
|`.data <addr>`| Indica que los siguientes ítems son datos (variables) y deben almacenarse en el segmento de datos. Si el argumento opcional *addr* está presente, los ítems son almacenados desde la dirección *addr*.|
|`.align n` | Alinear el siguiente dato en una posición de memoria divisible por 2<sup>n</sup>. Por ejemplo, `.align 2` alinea el siguiente valor en una dirección divisible por 4 (alineado a word) límite de palabra.|
|`.align 0` | Desactiva la alineación automática de las directivas `.half`, `.word`, `.float` y `.double` hasta la siguiente directiva `.data`.|
|`.ascii str`|Almacena el string en memoria pero no agrega byte nulo al final.|
|`.asciiz str`| Almacena el string en memoria y agrega byte nulo al final.|
|`.byte b1, ..., bn`| Almacena los n valores en bytes sucesivos en memoria.|
|`.half h1, ..., hn`|Almacena los n valores de 16 bits en halfwords sucesivos en memoria.|
|`.word w1, ..., wn` |Almacena los n valores de 32 bits en words sucesivos en memoria.|
|`.float f1, ..., fn` |Almacena los n flotantes de precisión simple sucesivos en memoria.|
|`.double d1, ..., dn` |Almacena los n flotantes de precisión doble sucesivos en memoria.|
|`.comm sym size` |Aloca size bytes en el segmento de datos para el símbolo sym.|
|`.global sym`|Declara que el símbolo sym es global y que puede ser referenciado desde otros archivos.|
|`.label sym`|Declara que el símbolo sym es una etiqueta.|
|`.text <addr>`|Indica que los siguientes ítems en memoria son instrucciones. Si el argumento opcional addr está presente, los ítems son almacenados desde la dirección addr.|
|`.end`|Marca el fin del archivo del módulo del programa.|

## ARM - Set de instrucciones
### Características principales 
- Arquitectura Load/Store: la forma de comunicarse con la memoria es solamente a través de Load y Store
- Instrucciones de longitud fija (32 bits) 
- Formatos de instrucciones de 3 direcciones:
    - 2 registros de operacion 
    - 1 registro de resultado
- Ejecución condicional de todas las instrucciones: permite que las instrucciones se ejecuten si se cumplen ciertas instrucciones
- Existen instrucciones de Load-Store de registros múltiples. Si se quiere cargar info de una dirección de memoria se puede hacer de una a varios registros. 

### Formato de instrucciones
Cada instrucción es codificada en una 32-bit word.

![aaa](https://github.com/user-attachments/assets/268cb383-83d2-41ed-8352-d9a2d18d35bc)

Una instrucción especifica un código de ejecución condicional (Condition), el código OP (OP code), dos o tres registros (Rn, Rd y Rm) y alguna otra información adicional.

### Ejecucion condicional
Una característica distintiva y algo inusual de los procesadores ARM es que todas las instrucciones se ejecutan condicionalmente dependiendo de una condición especificada en la instrucción.

La instrucción es ejecutada sólo si el estado actual del flag del código de condición del procesador satisface la condición especificada. Por lo tanto, las instrucciones cuya condición no se ve satisfecha en el flag de código de condición del procesador no se ejecutan. 

Una de las condiciones se utiliza para indicar que la instrucción siempre se ejecuta.

🟢 Esta característica elimina la necesidad de utilizar muchas bifurcaciones. El costo en tiempo de no ejecutar una instrucción condicional es frecuentemente menor que el uso de una bifurcación o llamado a una subrutina que, de otra manera, sería necesaria.

#### Ejemplo
```
	.equ SWI_Print_Int, 0x6B
	.equ SWI_Exit, 0x11

	.text
	.global _start
_start:
	mov r0, #4
	mov r1, #4
	cmp r0, r1                    @ Se compara r0 con r1, como son iguales se setea el ZF
	addeq r2, r0, r1              @ Como esta seteado el ZF se ejecuta la suma
	mov r1, r2
	mov r0, #1
	swi SWI_Print_Int
	swi SWI_Exit
```

Las instrucciones de procesamiento de datos no afectan a las *condition flags* (las instrucciones de comparacion si). Para que los condition flags se vean afectados, el bit S de la instrucción necesita estar seteado. Esto se hace agregando el sufijo S a la instrucción (y a cualquier código de condición).

#### Ejemplo 
Restar uno al r1 y afectar los condition flags en un loop
```
.loop: ...
    subs r1, r1, #1
    bne loop           @ si en la resta el resultado no fue 0 (los dos valores iguales), se vuelve al loop
```

