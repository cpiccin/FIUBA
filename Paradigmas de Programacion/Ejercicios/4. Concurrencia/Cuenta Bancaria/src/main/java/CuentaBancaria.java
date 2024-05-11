import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class CuentaBancaria {
    private int saldo = 30;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition saldoSuficiente = lock.newCondition();

    public int verSaldo() {
       lock.lock();
       try {
           return saldo;
       } finally {
           lock.unlock();
       }
    }

    public void depositar(int cantidad) {
        lock.lock();
        try {
            saldo += cantidad;
            saldoSuficiente.signal();
        } finally {
            lock.unlock();
        }
    }


    public void extraer(int cantidad) throws InterruptedException {
        lock.lock();
        try {
            if (saldo < cantidad) {
                saldoSuficiente.await();
            }
            saldo -= cantidad;
        } finally {
            lock.unlock();
        }
    }
}

