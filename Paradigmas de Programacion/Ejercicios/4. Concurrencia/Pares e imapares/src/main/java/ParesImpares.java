import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ParesImpares {
    final int nFinal = 200;
    boolean esPar = true;
    final Lock lock = new ReentrantLock();
    final Condition condTurnoPares = lock.newCondition();
    final Condition condTurnoImpares = lock.newCondition();

    private void imprimirPares() {
        int n = 0;
        while (n < nFinal) {
            lock.lock();
            while (!esPar) { // si el numero actual es par
                 try {
                     condTurnoPares.await();
                 } catch (InterruptedException e) {
                     throw new RuntimeException(e);
                 }
            }
            System.out.println("par: " + n);
            n += 2;
            esPar = false;
            condTurnoImpares.signal();
            lock.unlock();
        }
    }

    private void imprimirImpares() {
        int n = 1;
        while (n < nFinal) {
            lock.lock();
            while (esPar) { // si el numero actual es impar
                try {
                    condTurnoImpares.await();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
            System.out.println("impar: " + n);
            n += 2;
            esPar = true;
            condTurnoPares.signal();
            lock.unlock();
        }
    }

    public void imprimirTodo() throws InterruptedException {
        Thread hPares = new Thread(this::imprimirPares, "pares");
        Thread hImpares = new Thread(this::imprimirImpares, "impares");

        hPares.start();
        hImpares.start();

        hPares.join();
        hImpares.join();
    }

    public static void main(String[] args) throws InterruptedException {
        ParesImpares n = new ParesImpares();
        n.imprimirTodo();
    }

}
