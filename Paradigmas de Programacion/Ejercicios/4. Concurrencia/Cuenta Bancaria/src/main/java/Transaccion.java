public class Transaccion implements Runnable {
    private final CuentaBancaria origen;
    private final CuentaBancaria destino;
    private final int cantidad;
    private final String nombre; // Nuevo campo

    public Transaccion(CuentaBancaria origen, CuentaBancaria destino, int cantidad, String nombre) {
        this.origen = origen;
        this.destino = destino;
        this.cantidad = cantidad;
        this.nombre = nombre; // Inicializar el nuevo campo
    }

    @Override
    public void run() {
        if (origen.verSaldo() >= cantidad) {
            try {
                origen.extraer(cantidad);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            destino.depositar(cantidad);
            System.out.println("cantidad: "+cantidad);
            System.out.println("Transaccion " + nombre + ": Saldo cuenta origen: " + origen.verSaldo());
            System.out.println("Transaccion " + nombre + ": Saldo cuenta destino: " + destino.verSaldo());
        } else {
            System.out.println("Transaccion " + nombre + ": No hay suficiente saldo en la cuenta origen.");
        }
    }
}