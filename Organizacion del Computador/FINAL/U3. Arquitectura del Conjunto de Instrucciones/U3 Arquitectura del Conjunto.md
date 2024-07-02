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
- Las microarquitecturas cableadas son típicamente más rápidas para las operaciones que están directamente soportadas por el hardware, pero pueden ser menos flexibles que las arquitecturas basadas en microcódigo, ya que cualquier cambio o adición al conjunto de instrucciones requiere modificaciones físicas en el hardware.

### Microprogramada ("software")
- El como se ejecutan las cosas dentro del CPU se define mediante microcodigo en el hardware, secuencias de operaciones más simples, definidas por un microcódigo.
- El conjunto de instrucciones del procesador no está directamente codificado en el hardware, sino que es definido por el microcódigo almacenado en una memoria especial dentro del procesador.
- Las microarquitecturas microprogramadas pueden ser más lentas en la ejecución de instrucciones en comparación con las arquitecturas cableadas debido a la sobrecarga adicional de interpretar el microcódigo, pero ofrecen ventajas significativas en términos de flexibilidad, facilidad de diseño y capacidad para soportar un conjunto de instrucciones más complejo.

## ISA (Instruction Set Architecture) - Arquitectura de Programacion:
### Repertorio de instrucciones

### Especificacion de su operacion

### Registros

### Tipos de datos

### Modos de direccionamiento

### Formato de Instrucciones

### Memoria
  * Word size (byte, dword, qword, etc)
  * Big/Little Endian
  * Direccionamiento
  * Espacio de direcciones

