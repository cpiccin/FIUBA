import java.util.ArrayList;
import Usuario.Usuario;
import Mensaje.Mensaje;
public class Sistema {
    private ArrayList<Usuario> usuarios;
    private Usuario usuarioActual;
    private boolean sistemaAbierto;

    public Sistema() {
        this.usuarios = new ArrayList<Usuario>();
        this.usuarioActual = null;
        this.sistemaAbierto = true;
    }

    public void agregarUsuario(Usuario usuario) {
        if (this.usuarios.contains(usuario)) {
            //el usuario ya existe
            return;
        }
        this.usuarios.add(usuario);
    }

    public boolean iniciarSesion(String nombre, String contra) {
        Usuario iniciarUsuario = buscarUsuario(nombre);
        if (iniciarUsuario == null) {
            return false; // el user no existe
        }
        if (!iniciarUsuario.getContrasena().equals(contra)) {
            return false; // contra incorrecta
        }
        usuarioActual = iniciarUsuario;
        return true;
    }

    public void registrarUsuario(String nombre, String contra, boolean personal) {
        if (buscarUsuario(nombre)==null) {
            return; // el user ya existe
        }
        Usuario nuevo = new Usuario(nombre, contra, personal);
        usuarios.add(nuevo);

    }

    private Usuario buscarUsuario(String nombre) {
        for (Usuario user : usuarios) {
            if (user.getNombre().equals(nombre)) {
                return user;
            }
        }
        return null;
    }

    public boolean enviarMensaje(String recep, Mensaje mensaje) {
        Usuario receptor = buscarUsuario(recep);
        if (receptor == null) {
            return false; //el receptor no existe
        }
        usuarioActual.enviarMensaje(mensaje);
        receptor.recibirMensaje(mensaje);
        return true;
    }
    public boolean crearNuevaCuenta(String nombre, String contra, boolean personal) {
        if (!usuarioActual.getCargo()) {
            return false; // no tiene permisos
        }
        if (buscarUsuario(nombre) == null) {
            return false; // el user ya existe
        }
        Usuario nuevo = new Usuario(nombre, contra, personal);
        usuarios.add(nuevo);
        return true;
    }

    public void cerrarSesion() {
        usuarioActual = null;
    }

    public boolean cerrarSistema() {
        if (usuarioActual == null || !usuarioActual.getCargo()) {
            return false; // no hay usuario logeado o no tiene permisos
        }
        sistemaAbierto = false;
        return true;
    }

    public void mostrarEnviados() {
        for (Mensaje mensaje : usuarioActual.getMensajesEnviados()) {
            System.out.println("De: " + mensaje.getEmisor() + " Para: " + mensaje.getReceptor() + "\nContenido: " + mensaje.getContenido()+"\n");
        }
    }
    public void mostrarRecibidos() {
        for (Mensaje mensaje : usuarioActual.getMensajesRecibidos()) {
            System.out.println("De: " + mensaje.getEmisor() + " Para: " + mensaje.getReceptor() + "\nContenido: " + mensaje.getContenido()+"\n");
        }
    }
}
