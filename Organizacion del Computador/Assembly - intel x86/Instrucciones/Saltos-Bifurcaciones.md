# Saltos/Bifurcaciones

- JMP op
Bifurca a la direccion indicada por el operando

- Jcc op
Bifurca a la direccion indicada del operando si se cumple la condicion.


## Llamada y Retorno de procedimiento
- CALL op
Almacena en la pila la direccion de la instruccion siguiente a la call y bifurca al punto indicado por el operando

- RET op
Toma el elemento del tope de la pila que debe ser una direccion de memoria y bifurca hacia la misma.

## Condicionales

### Generales
ZF = Zero Flag ; CF = Carry Flag ; OF = Overflow Flag
- JE op     -> si son iguales ZF=1
- JNE op    -> si no son iguales ZF=0
- JZ op     -> si es igual a cero ZF=1
- JNZ op    -> si es distinto a cero ZF=0
- JRCXZ op  -> si el contenido del RCX es cero, salta a la label op si es cero, si no sigue
- JC op     -> si CF es distinto de cero CF=1
    * The Carry Flag is set by previous arithmetic instructions (like ADD, SUB, MUL, etc.) if an operation resulted in a carry out of the most significant bit (for addition) or a borrow into the most significant bit (for subtraction).
    * The JC instruction checks the Carry Flag. If CF is 1 (indicating a carry or borrow occurred), it jumps to the specified label in the program. If CF is 0 (indicating no carry or borrow occurred), it continues to the next instruction.
- JO op     -> si hubo overflow (OF=1)
