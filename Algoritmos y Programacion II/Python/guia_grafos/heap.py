import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def encolar(self, item, prioridad):
        heapq.heappush(self.heap, (prioridad, item))
    
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("El heap está vacío")
        return heapq.heappop(self.heap)[1]
    
    def esta_vacia(self):
        return len(self.heap) == 0

    def __str__(self):
        res = "["
        for n in self.heap:
            if n == self.heap[-1][1]:
                res += str(n[1])
                break
            res += str(n[1]) + ", "
        return res + "]"


class MaxHeap:
    def __init__(self):
        self.heap = []

    def encolar(self, item, prioridad):
        heapq.heappush(self.heap, (-prioridad, item))

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("El heap está vacío")
        return -heapq.heappop(self.heap)[1]

    def esta_vacia(self):
        return len(self.heap) == 0

    def __str__(self):
        res = "["
        for n in self.heap:
            if n == self.heap[-1][1]:
                res += str(n[1])
                break
            res += str(n[1]) + ", "
        return res + "]"

