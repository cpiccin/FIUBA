(ns capicua.core
  (:gen-class))

;; Definir la función capicua? que reciba un número entero no negativo de hasta 5 dígitos 
;; y devuelva true si el número es capicúa si no, false.


(defn capicua? [n]
  (= (str n) (apply str (reverse (seq (str n))))))
;; apply convierte a cada caracter de la secuencia en str y los concatena


(defn -main [& args]
  (def n 23432)
  (print(capicua? n))
  )
