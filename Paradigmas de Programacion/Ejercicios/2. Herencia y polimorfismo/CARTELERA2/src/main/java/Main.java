import Usuario.Usuario;
import Mensaje.Mensaje;

public class Main {
    public static void main(String[] args) {
        // Create a Sistema object
        Sistema sistema = new Sistema();

        // Create some Usuario objects
        Usuario usuario1 = new Usuario("Alice", "password1", true);
        Usuario usuario2 = new Usuario("Bob", "password2", false);

        // Add the Usuario objects to the Sistema
        sistema.agregarUsuario(usuario1);
        sistema.agregarUsuario(usuario2);

        // Create some Mensaje objects
        Mensaje mensaje1 = new Mensaje("Hello, Bob!", "Alice", "Bob");
        Mensaje mensaje2 = new Mensaje("Hi, Alice!", "Bob", "Alice");

        // Alice logs in and sends a message to Bob
        sistema.iniciarSesion("Alice", "password1");
        sistema.enviarMensaje("Bob", mensaje1);

        // Alice checks her sent messages
        System.out.println("Alice's sent messages:");
        sistema.mostrarEnviados();

        // Alice logs out
        sistema.cerrarSesion();

        // Bob logs in and sends a message to Alice
        sistema.iniciarSesion("Bob", "password2");
        sistema.enviarMensaje("Alice", mensaje2);

        // Bob checks his sent messages
        System.out.println("Bob's sent messages:");
        sistema.mostrarEnviados();

        // Bob checks his received messages
        System.out.println("Bob's received messages:");
        sistema.mostrarRecibidos();

        // Bob logs out
        sistema.cerrarSesion();
    }
}
