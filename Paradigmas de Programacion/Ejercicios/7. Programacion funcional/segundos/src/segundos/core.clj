(ns segundos.core
  (:gen-class))

;; Definir la función segundos que reciba los cuatro valores (días, horas, minutos y segundos) 
;; del tiempo que dura un evento y devuelva el valor de ese tiempo expresado solamente en segundos.

(defn segundos [d h m s]
  (let [s (+ (* m 60) (* h 3600) (* d 86400))]
    s))

(defn -main []
  (print (segundos 2 3 20 0)))