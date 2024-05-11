public class Main {
    public static void main(String[] args) {
        Sistema cartelera = new Sistema();
        cartelera.abrirSistema();
        cartelera.registrarUsuario("juan", "123", false);
        boolean inicioExitoso = cartelera.iniciarSesion("Lucas", "123", false);
        if (!inicioExitoso) {
            System.out.println("No se pudo iniciar sesion. Usuario no registrado");
        }
        cartelera.registrarUsuario("Lucas", "123", false);
        inicioExitoso = cartelera.iniciarSesion("Lucas", "123", false);
        if (inicioExitoso) {
            System.out.println("Inicio de sesion exitoso");
        }
        cartelera.enviarMensaje("juan", "Hola, como estas?");
        cartelera.enviarMensaje("juan", "me vas a responder, amigazo?");
        cartelera.enviarMensaje("juan", "no me dejes en visto");
        cartelera.enviarMensaje("juan", "dale loco, contesta");
        cartelera.verMensajes();

        cartelera.cerrarSesion();
        cartelera.registrarUsuario("Jefe", "433", true);
        cartelera.iniciarSesion("juan", "123", false);
        //cartelera.verMensajes();



    }
}
