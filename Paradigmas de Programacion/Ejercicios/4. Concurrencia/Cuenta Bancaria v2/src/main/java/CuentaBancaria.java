import java.util.concurrent.locks.ReentrantReadWriteLock;

public class CuentaBancaria {
    private int saldo = 30;
    private final ReentrantReadWriteLock lock = new ReentrantReadWriteLock();

    public void depositar(int cantidad) {
        lock.writeLock().lock();
        try {
            saldo += cantidad;
        } finally {
            lock.writeLock().unlock();
        }
    }

    public void extraer(int cantidad) throws InterruptedException {
        lock.writeLock().lock();
        try {
            while (saldo < cantidad) {
                // Esperar hasta que haya suficiente saldo
            }
            saldo -= cantidad;
        } finally {
            lock.writeLock().unlock();
        }
    }

    public int verSaldo() {
        lock.readLock().lock();
        try {
            return saldo;
        } finally {
            lock.readLock().unlock();
        }
    }
}