(ns sistemasl.core
  (:gen-class)
  (:require [clojure.string :as str]))

; -- Constantes --
(def longitud 10)
(def vuelta-entera 180)

(defn grados-a-rad
  "Esta funcion transforma a radianes el grado recibido"
  [deg]
  (/ (* deg Math/PI) 180))

(defn mover
  "Esta funcion toma el valor X e Y y devuelve un movimiento tomando en cuenta el angulo actual"
  [x y angulo]
  ""
  (let [radianes (grados-a-rad angulo)
        nuevo-x (+ x (* longitud (Math/cos radianes)))
        nuevo-y (+ y (* longitud (Math/sin radianes)))]
    [nuevo-x nuevo-y]))

(defn redondear-coord
  "Esta funcion redondea las coordenadas"
  [coords]
  (map #(Math/round (double %)) coords))

(defn procesar-instruccion
  "Esta función procesa una instrucción individual en el contexto de la secuencia actual de instrucciones.

  Recibe como parametros:
    - estado: diccionario que contiene el estado actual. Incluye las claves :x, :y, :angulo, :pila, :lineas y :pluma-abajo.
    - comando: el carácter que representa la instrucción a procesar.
    - ang: un float que representa el ángulo de rotación.

  La función analiza el comando y realiza la acción correspondiente, actualizando el estado del sistema. Las acciones posibles son:

    - F y G: Mueve el sistema en la dirección actual del ángulo.
    - f y g: Mueve el sistema en la dirección actual del ángulo sin añadir una línea al estado, indica que la pluma esta arriba.
    - -: Rota el proximo movimiento hacia la izquierda un angulo ang.
    - +: Rota el proximo movimiento hacia la derecha  un angulo ang.
    - |: Rota el proximo movimiento 180 grados
    - [: Indica que comienza una nueva tortuga.
    - ]: Indica que finaliza la tortuga actual.

  La función devuelve el estado del sistema después de procesar la instrucción."
  [estado comando ang]
  (let [{:keys [x y angulo pila lineas pluma-abajo]} estado] ; se extraen los valores de estado en esas keys para no tenes que llamar a esos datos con get
    (case comando
      (\F \G) (let [[nuevo-x nuevo-y] (mover x y angulo)]
           {:x nuevo-x :y nuevo-y :angulo angulo :pila pila :pluma-abajo pluma-abajo
            :lineas (if pluma-abajo (conj lineas (redondear-coord [x y nuevo-x nuevo-y])) lineas)})
      (\f \g) (let [[nuevo-x nuevo-y] (mover x y angulo)]
           {:x nuevo-x :y nuevo-y :angulo angulo :pila pila :pluma-abajo pluma-abajo :lineas lineas})
      \- (update estado :angulo - ang) ;
      \+ (update estado :angulo + ang)
      \| (update estado :angulo + vuelta-entera)
      \[ (update estado :pila conj [x y angulo pluma-abajo])
      \] (let [[x-anterior y-anterior angulo-anterior pluma-abajo-anterior] (peek pila)]  ; veo tope y extraigo valores solo porque se entiende mejor
           {:x x-anterior :y y-anterior :angulo angulo-anterior :pluma-abajo pluma-abajo-anterior :pila (pop pila) :lineas lineas}) ; se desapila la tortuga porque se termino y se vuelve al estado anterior
      estado)))

(defn procesar-cadena
  "Procesa una secuencia de comandos representada por la cadena de entrada.

  La función toma dos argumentos: entrada y angulo. entrada es una secuencia de caracteres que representan comandos, y `angulo` es el ángulo inicial.

  La función recorre cada comando en la secuencia de entrada y llama a la función procesar-instruccion para cada uno.

  El estado inicial es un mapa con las claves: :x, :y, :angulo, :pila, :pluma-abajo, :lineas.

  La función devuelve el estado final después de procesar todos los comandos en la secuencia de entrada."
  [entrada angulo]
  (reduce (fn [estado instruccion]
            (procesar-instruccion estado instruccion angulo))
          {:x 0 :y 0 :angulo 0 :pila [] :pluma-abajo true :lineas []}
          (filter #(not (#{\X \Y} %)) entrada))) ; elimina de la cadena los X e Y para que queden solo las instrucciones

(defn generar-lineas
  "Genera una estructura segun la secuencia de instrucciones recibidas y el angulo"
  [secuencia angulo]
  (:lineas (procesar-cadena secuencia angulo)))

(defn min-max-coords
  "Recibe la secuencia de instrucciones ya procesadas y obtiene los minimos y maximos X e Y."
  [lineas]
  (let [todas-coords (flatten lineas)
        xs (take-nth 2 todas-coords)
        ys (take-nth 2 (rest todas-coords))]
    {:min-x (apply min xs)
     :max-x (apply max xs)
     :min-y (apply min ys)
     :max-y (apply max ys)}))

(defn crear-svg
  "Recibe la secuencia de instrucciones y el nombre de un archivo
  Genera una secuencia de lineas en formato SVG y se escriben en el archivo"
  [lineas {:keys [min-x max-x min-y max-y]} nombre-archivo]
  (let [ancho  (- max-x min-x)
        alto (- max-y min-y)
        vista (str min-x " " min-y " " ancho " " alto)
        encabezado-svg (str "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"" vista "\" width=\"" ancho "\" height=\"" alto "\">")
        pie-svg "</svg>"
        lineas-svg (apply str (map (fn [[x1 y1 x2 y2]]
                                     (str "<line x1=\"" x1 "\" y1=\"" y1 "\" x2=\"" x2 "\" y2=\"" y2 "\" stroke=\"black\" stroke-width=\"1\" />"))
                                   lineas))]
    (spit nombre-archivo (str encabezado-svg lineas-svg pie-svg))))

(defn crea-diccionario
  "Pasa a diccionario el vector recibido con un formato especifico"
  [vector]
  (into {} (for [s vector]
             (let [[k v] (str/split s #" ")]
               [(str k) v]))))

(defn leer-archivo
  "Recibe el nombre del archivo a leer

  Lee el archivo desde la carpeta 'resources' y devuelve un vector

  Lee el contenido del archivo como una cadena de texto;
  divide la cadena en lineas y las guarda en un vector;
  divide el vector en dos: 1. angulo+estado inicial, 2.reglas del sistema;
  convierte las reglas del sistema en un diccionario.

  Devuelve un vector que contiene las dos primeras lineas y el diccionario:
  [angulo, estado inicial, {reglas}]
  "
  [archivo-sl]
  (let [ruta (str "resources/" archivo-sl)]
      (let [contenido (slurp ruta)
            lineas (vec (str/split-lines contenido))
            resultado (conj (subvec lineas 0 2) (crea-diccionario(subvec lineas 2 (count lineas))))]
        resultado)))

(defn aplicar-reglas
  "Recibe:
      - s : estado actual del sistema
      - reglas : diccionario con las reglas del sistema

  La función recorre cada carácter en el estado actual `s`. Para cada carácter, busca su correspondiente en el diccionario `reglas`. Si el carácter no se encuentra en el diccionario, se utiliza el carácter original.

   Devuelve:
      - cadena-final : estado final del sistema después de aplicar todas las reglas."
  [s reglas]
  (reduce (fn [cadena-final char-actual]
            (str cadena-final (get reglas (str char-actual) (str char-actual))))
          ""
          s))

(defn generar-secuencia
  "Recibe:
        - s : estado inicial del sistema
        - reglas : diccionario con las reglas del sistema
        - n : cantidad de iteraciones

  Itera recursivamente n veces aplicando las reglas del sistema al estado inicial.
  En cada iteracion se aplica la funcion aplicar-reglas al estado actual"
  [s reglas n]
  (if (zero? n)
    s
    (recur (aplicar-reglas s reglas) reglas (dec n))))

(defn -main [& args]
  (let [[archivo-sl iteraciones nombre-svg] args
    texto-archivo-sl (leer-archivo archivo-sl)
    secuencia-completa (generar-secuencia (nth texto-archivo-sl 1) (nth texto-archivo-sl 2) (Integer/parseInt iteraciones))
    angulo (Float/parseFloat (nth texto-archivo-sl 0))
    lineas (generar-lineas secuencia-completa angulo)
    coords (min-max-coords lineas)]
    (crear-svg lineas coords nombre-svg)
    ))




