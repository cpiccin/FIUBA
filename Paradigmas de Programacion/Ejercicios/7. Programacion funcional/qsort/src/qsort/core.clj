(ns qsort.core
  (:gen-class))

;; Definir la función qsort que recibe una secuencia y la ordena usando el algoritmo Quicksort.

(defn qsort [secuencia] 
  (if (empty? secuencia)
    secuencia
    (let [pivot (first secuencia)
          ;; Devuelve una secuencia seleccionando los datos del segundo argumento que cumplan con el predicado indicado como primer argumento.
          izq (filter #(< % pivot) (rest secuencia)) ;; #(< % pivot) es una funcion anonima que toma un argumento representado por % y chequea si es menor al pivot
          med (filter #{pivot} secuencia) ;; #{pivot} es un set que contiene a pivot. Chequea si cada elemento de la seq esta en el set y filtra aquellos elementos iguales al pivot 
          der (filter #(> % pivot) (rest secuencia))] ;; #(< % pivot) es una funcion anonima que toma un argumento representado por % y chequea si es mayor al pivot
      (concat (qsort izq) med (qsort der)))))


(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println(qsort (seq [3 2 4 2 1]))))
