(ns untitled.core)


(defn suma3 [a b c]
  (+ a b c))

(defn -main []
  (println ((fn [x y] [y x]) ((fn [x] x) ((fn [z] 'w) 'u)) ((fn [y] y) 'v))))

