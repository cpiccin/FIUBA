## Monads 
Un monad es un _patron de diseño_ que permite encadenar operaciones mientras que el monad se encarga por atras de realizar estas tareas.
En Programación Funcional, un monad es una estructura que combina funciones, definiendo un tipo monádico envolvente (wrapper type) y dos operadores: uno para envolver un valor en el tipo monádico (wrap function) y otro para componer funciones y producir un valor del tipo monádico (run function).
Todos los monadas tienen tres componentes:
1. <ins>Wrapper Type</ins>: algun wrapper que define el tipo del monad.
2. <ins>Wrap Function</ins>: funcion que toma valores normales y los wrappea en el monad, como si fuese un constructor. Se identifican como ```return, pure, unit```.
3. <ins>Run Function</ins>: toma el wrapper type y una **funcion de transformacion** que acepta al unwrapped type (el valor normal) y que devuelve el wrapper type. Se identifican como ```bind, flatMap, >>=```.

### Option/Maybe Monad
Representa la posible no existencia un valor
Ejemplo: n puede ser que tenga un numero o que no tenga nada. Null o indefinido pero usando un tipo definido. Mejora el manejo de nulls, por ejemplo si algo tira NullPointerException, en vez del error va a devolver nill directamente. El trabajo por detras de este monad es el manejo de posibles valores inexistentes.
```
Option<int> = n   int or null/undefined
```
1. Wrapper Type: ```Option<T>``` puede wrappear cualquier tipo T generico.
2. Wrap Funcion: toma valores de tipo T y los wrappea en un Option devolviendo ```Option<T>```. En este monad se llama ```func some<T> {}```
3. Run Function: toma el tipo Option y la funcion de transformacion

### Furure/Promise Monad
Representa la idea de que un valor puede no estar listo en ese momento, o sea que puede ser asincronico y estar disponible mas tarde.

### Either Monad
Representa un calculo que puede resultar en un valor correcto (Right) o en un error (Left). 
Permite manejar errores y excepciones sin usar excepciones del lenguaje, dando un flujo de control mas claro.

### State Monad 
Maneja y pasa un estado mutable a través de una secuencia de cálculos.
Permite implementar algoritmos que necesitar mantener y actualizar un estado sin utilizar mutabilidad explicita.

### List Monad
Representa cálculos no deterministas que pueden tener múltiples resultados.
Permite modelar computaciones que pueden producir múltiples resultados, como la generación de combinaciones o permutaciones.

hay un monton mas...

## Funtores
Un funtor es algo sobre lo que se puede mappear (significando que a ese algo se le puede aplicar una funcion a todos sus valores, al final recolocandolos en un nuevo contenedor con la misma forma y estructura)
Segun Corsi: "Un funtor es cualquier tipo de datos que define cómo `fmap` se comporta para su caso."
```
Unwrap value  --->  Apply    --->  Rewrap value
from context       function         in context
```
```
No value, ---> Don't apply  --->  End up with
nothing         function           nothing
```
