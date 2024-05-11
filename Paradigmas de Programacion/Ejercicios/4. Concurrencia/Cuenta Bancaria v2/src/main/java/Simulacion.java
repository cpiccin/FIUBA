import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Simulacion {
    public static void main(String[] args) {
        int M = 3; // Número de cuentas
        int N = 4; // Número de transacciones
        int T = 2; // Número de hilos

        // Crear M cuentas bancarias
        List<CuentaBancaria> cuentas = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            cuentas.add(new CuentaBancaria());
        }

        // Crear N transacciones
        List<Transaccion> transacciones = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < N; i++) {
            CuentaBancaria origen = cuentas.get(random.nextInt(M));
            CuentaBancaria destino;
            do {
                destino = cuentas.get(random.nextInt(M));
            } while (origen == destino); // Asegurarse de que origen y destino sean diferentes

            int cantidad = random.nextInt(10) + 1; // Cantidad a transferir
            String nombre = "Transaccion" + (i + 1); // Nombre único para la transacción
            transacciones.add(new Transaccion(origen, destino, cantidad, nombre));
        }

        // Crear un ExecutorService con T hilos
        ExecutorService executor = Executors.newFixedThreadPool(T);

        // Enviar las transacciones al ExecutorService para su ejecución
        for (Transaccion transaccion : transacciones) {
            executor.execute(transaccion);
        }

        // Cerrar el ExecutorService
        executor.shutdown();
    }
}