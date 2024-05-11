import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class ColaSincronizada<T>  {
    private final int capacidadMaxima;
    private List<T> datos;
    private int cantidadActual;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition sePuedeEncolar = lock.newCondition();
    private final Condition sePuedeDesencolar = lock.newCondition();


    public ColaSincronizada(int n) {
        capacidadMaxima = n;
        datos = new ArrayList<>();
        cantidadActual = 0;
    }

    public void encolar(T elem) {
        BlockingQueue<T>
    }

    public void desencolar() {
        
    }

    private boolean estaVacia() {
        return cantidadActual == 0;
    }

    private boolean estaLlena() {
        return cantidadActual == capacidadMaxima;
    }

    public void printCola() {
        System.out.println(Arrays.toString(datos.toArray()));
    }


}
