# U3 - Arquitectura del Conjunto de Instrucciones

## Arquitectura de computadoras: que puede hacer.
Son las caracteristicas computacionales visibles al programador, los atributos que tienen impacto directo en la ejecucion logica de un programa. Refiere al set de herramientas disponibles para el programador.

## Organizacion de computadoras: como lo hace.
Es la implementacion de la arquitectura (microarquitectura). Define las unidades operativas y sus interconexiones (señales de control, interfaces entre el CPU y los
periféricos, tecnología de memoria, trayecto de datos, etc.). <br>
Por ejemplo, el como la instruccion de multiplicar se ejecuta internamente (por sumas sucesivas u otro circuito electronico). <br>
<ins>*Distintas versiones comerciales de un computador alineadas a una misma arquitectura.*</ins> <br>
<br>
Pueden haber diferentes implementaciones de una misma arquitectura por un proposito comercial donde varian:
- Costos
- Velocidad de procesamiento
- Consumo de energia

La microarquitectura es la implementación específica de una arquitectura de computadora en términos de la organización y diseño de sus componentes internos. Hay dos maneras genericas de construir esa microarquitectura. Se construye esa organizacion de forma:

### Cableada (hardware)
- Es un diseño de microarquitectura en el cual las instrucciones y su ejecución están directamente implementadas mediante el hardware.
- Las operaciones y el flujo de control están codificados en la lógica física del procesador a través de circuitos, sin necesidad de un microcódigo o software intermedio para interpretar las instrucciones.
- Son típicamente más rápidas para las operaciones que están directamente soportadas por el hardware, pero pueden ser menos flexibles que las arquitecturas basadas en microcódigo, ya que cualquier cambio o adición al conjunto de instrucciones requiere modificaciones físicas en el hardware.

### Microprogramada ("software")
- El como se ejecutan las cosas dentro del CPU se define mediante microcodigo en el hardware, secuencias de operaciones más simples, definidas por un microcódigo.
- El conjunto de instrucciones del procesador no está directamente codificado en el hardware, sino que es definido por el microcódigo almacenado en una memoria especial dentro del procesador.
- Pueden ser más lentas en la ejecución de instrucciones en comparación con las arquitecturas cableadas debido a la sobrecarga adicional de interpretar el microcódigo, pero ofrecen ventajas significativas en términos de flexibilidad, facilidad de diseño y capacidad para soportar un conjunto de instrucciones más complejo.

## Familia de computadoras
Se refiere a una 
- Misma arquitectura base, distintas organizaciones (implementaciones).
- Modelos con prestaciones y precios diferentes pero compatibles entre sí.

## Modelo de capas
División de la arquitectura de computadoras en capas de forma jerárquica, cada capa interactua con la capa inferior o superior. <br>
![capas](https://github.com/cpiccin/FIUBA/assets/103950114/551eb875-fdae-4d19-b671-bf4b028d16a6)

### Software:

1. **Level 6 - Problem Oriented Language Level (Translation-Compiler):** This is the level of high-level programming languages like Python, Java, C++, etc. These languages are designed to be easy for humans to read and write. They are translated into machine code by compilers.

2. **Level 5 - Assembly Language Level (Translation-Assembler):** Assembly language is a low-level programming language specific to a particular computer architecture. It is converted into executable machine code by a utility program referred to as an assembler.

3. **Level 4 - Operating System Machine Level (Partial Interpretation):** This level is where the operating system resides. The OS interacts directly with the hardware and provides services to the higher level software.

4. **Level 3 - Instruction Set Architecture Level (Interpretation/Direct Execution):** This is the level of the raw machine code that is executed directly by the CPU. It is the interface between the hardware and the software.

### Hardware:

1. **Level 2 - Micro-architecture Level (Registers):** This level includes the CPU's data storage elements, such as registers and caches, and the execution units that perform operations on the data.

2. **Level 1 - Digital Logic Level (Gates):** This level is where the actual logic gates that make up the CPU are found. These gates perform basic binary logic operations like AND, OR, and NOT.

3. **Level 0 - Device Level (Individual Transistors):** This is the lowest level, where individual transistors, the building blocks of digital circuits, are found. Transistors act as electronic switches that open and close to control the flow of electricity and represent binary data.

## Clasificacion de computadoras segun su poder de calculo
| Supercomputadoras                  | Macrocomputadoras o Mainframes | Minicomputadoras o servidores middle range | Microcomputadoras / PC |Computadoras portátiles / notebooks / netbooks | Computadoras de mano |
|------------------------------------|--------------------------------|--------------------------------------------|------------------------|-----------------------------------------------|----------------------|
| Extremadamente rápidas             | Muy rapidas| Rapidas | Uso individual o redes pequeñas a medianas | Uso individual portátil | Uso individual portatil acotado |
| Manejan volúmenes de datos enormes | Manejan volúmenes de datos muy grandes| Manejan volumenes de datos grandes | Manejan volúmenes de datos no muy grandes | Manejan volúmenes de datos no muy grandes | Manejan volúmenes de datos pequeños |
| Poseen miles de CPU                | Poseen cientos de CPU| Poseen decenas de CPU |Poseen uno o varios CPU|Poseen uno o varios CPU|Poseen uno o varios CPU|
| Tienen usos específicos: militar, simulacion, ciencia            | Muy alta disponibilida y usos comerciales y cientificos: sistemas bancarios, telecomunicaciones, instituciones gubernamentales | Usos comerciales: empresas medianas y grandes, varios equipos en una misma empresa | Uso hogareño, educativo, comercial, recreativo: computadora del hogar, negocios, colegios, consolas de videojuegos |Uso hogareño, educativo, comercial, recreativo: estaciones de trabajo en empresas, computadora del hogar, negocios, colegios, consolas de videojuegos | Uso hogareño, comercial: Acopio de datos en vía pública, información personal, visualización de contenidos |

## Arquitectura Harvard
![harvarf](https://github.com/cpiccin/FIUBA/assets/103950114/b6eaf4b2-fa5a-425e-987b-3118703bc3c8)
![Screenshot from 2024-07-02 18-09-22](https://github.com/cpiccin/FIUBA/assets/103950114/0e4236dc-a408-4bca-96a1-62940e7f8e1f) <br>
La memoria de la maquina esta subdividida en dos espacios distintos, una para almacenar datos y otra para almacenar las instrucciones, el programa que hace uso de esos datos.<br>
Ahora el CPU interactua con dos memorias, cada una con un bus dedicado.
#### Puntos a considerar:
- La ventaja de tener dos memorias independientes tiene que ver con poder acceder de forma simuntanea a una instruccion y a un dato, poder cargar al mismo tiempo instrucciones y datos (instruction fetch y data access en paralelo por distintos buses).
- Como dificultad esta que como hay dos memorias diferentes se manejan espacios de direcciones diferentes lo que dificulta la programacion al tener que hacer esa diferenciacion.
- Es implementado en algunos microcontroladores PIC y en procesadores de señales digitales. 
- Usado en los DSP (tipo especializado de microprocesador diseñado específicamente para realizar operaciones de procesamiento de señales digitales de manera eficiente) para streaming de datos:
 * Mayor ancho de banda de memoria. 
 * Ancho de banda más predecible. 
- En la práctica, las diferencias en el rendimiento de acceso entre las arquitecturas Harvard y Von Neumann pueden no ser tan significativas como en la teoría, especialmente en aplicaciones generales de propósito general. Además, la complejidad de la programación en una arquitectura Harvard puede limitar su uso en ciertos contextos.

|Diferencias de rendimiento|Complejidad de programacion|Aplicaciones especializadas|
|--------------------------|---------------------------|---------------------------|
| Teoricamente, Hardvard puede ofrecer ventajas por el acceso simultaneo a datos e instrucciones, pero en la practica no es tan notable ese rendimiento. Se debe a que otros factores como la velocidad de la memoria, la optimizacion del codigo, pueden influir mas en ese rendimiento general | La separacion de datos e instrucciones puede complejizar la programacion. Von Neumann tiene una abstraccion mas simple donde los datos y las instrucciones se manejan de manera mas uniforme. | Hardvard es mas adecuada para aplicaciones especializadas que necesiten un acceso rapido y eficiente a la memoria  como en sistemas embebidos, procesamiento de señales, control en tiempo real, etc.|

## ISA (Instruction Set Architecture) - Arquitectura de Programacion:

### Repertorio de instrucciones
Instrucciones de maquina; instrucciones que entiende nativamente el CPU. 

#### <ins>¿Qué es una instrucción de máquina?</ins> 
- Una instruccion que entiende directamente el CPU de la maquina.
- Las instrucciones son visibles para el CPU dentro del registro de instrucciones.
- Cuando la "ve" (hizo el fetch desde la memoria) va a la fase de la instruccion en si.
- Tiene la forma `Opcode + Operandos (0 a n)`

#### Categorias:
- Aritmeticas y logicas
  * add, substract, divide, multiply
  * and, or, xor
- Movimiento de datos
  * load, store, move
- Entrada / Salida
  * start I/O (input/output)
- Control de flujo
  * branch, jump, compare, call, return
  
#### Tipos de operandos
- Registro
- Memoria
- Inmediato

#### Clasificacion segun la ubicacion de los operandos
Segun la implementacion de la arquitectura cambia donde va a estar el operando para poder realizar la instruccion.
- Stack
- Acumulador (abacus)
- Registro-Memoria (superabacus)
- Registro-Registro (load-store) (suberabacus)
- Memoria-Memoria
Resolucion de `C = A + B` segun cada arquitectura:
![adsd](https://github.com/cpiccin/FIUBA/assets/103950114/74475f5f-c2bc-4c63-8777-9e213c54e9e1)

#### Clasificacion de la ISA segun el numero de direcciones
- 0 direcciones (Stack): add 
- 1 dirección (Acumulador): add A
- 2 direcciones (Reg-Mem/Reg-Reg/Mem-Mem): add R1, A
- 3 direcciones (Reg/Mem): add R1, R2, R3

### Tipos de datos
- Numéricos (BPF s/s, BPF c/s, BPFlotante, BCD). 
- Caracteres (ASCII, EBCDIC, Unicode) 
- Datos lógicos 
- Direcciones

### Modos de direccionamiento

### Formato de Instrucciones (Encoding)
Define como cada arquitectura especifica que campos y que bits componen cada instruccion.

#### Componentes
- Opcode
- 0 a n operandos
- Modo de direccionamiento de cada operando
- Flags

<ins> **Formato fijo** </ins>: todas las instrucciones de máquina tienen el mismo tamaño de instrucción, a pesar de poder tener distinto formato.
En **ARM** todas las instrucciones de ARM miden 32 bits<br>
<p>
  <img src="https://github.com/cpiccin/FIUBA/assets/103950114/b44adff2-76df-43b6-a3c5-2e8ba80f0b20" alt="arm" style="display: block; margin-left: auto; margin-right: auto; width: 300px;" />
</p>

<ins> **Formato variable** </ins>: el tamaño de las instrucciones de máquina depende de cómo se escriba la instrucción.<br>
En **x86** es un unico formato variable (el tamaño de cada campo es variable) <br>
<p>
  <img src="https://github.com/cpiccin/FIUBA/assets/103950114/4fa37d4e-80f5-4c35-8405-c9388534b4c3" alt="arm" style="display: block; margin-left: auto; margin-right: auto; width: 300px;" />
</p>

<ins> **Formato hibrido** </ins>: mezcla entre fijo y variable. Hay distintos formatos, cada uno tiene un tamaño definido, por lo que el tamaño depende de cómo combine los formatos. <br>
En **IBM Mainframe** el formato de instruccion varia pero cada uno a su vez es fijo


### Memoria
  * Word size (byte, dword, qword, etc)
  * Big/Little Endian
  * Direccionamiento
  * Espacio de direcciones

