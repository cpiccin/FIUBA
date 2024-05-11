import java.util.ArrayList;

public class Sistema {
    private boolean sistemaAbierto;
    private ArrayList<Usuario> usuarios = new ArrayList<>();
    private Usuario usuarioActual;

    public void abrirSistema() {
       this.sistemaAbierto = true;
    }
    public boolean sistemaEstaAbierto() {
        return sistemaAbierto;
    }
    public boolean iniciarSesion(String usuario, String contra, boolean esPersonal) {
        // devuelve true si el inicio de sesion fue exitoso, o sea el usuario estaba registrado previamente
        Usuario nuevoActual = buscarUsuario(usuario);
        if (nuevoActual != null) {
            usuarioActual = nuevoActual;
            return true;
        }
        return false;
    }
    public void registrarUsuario(String usuario, String contra, boolean personal) {
        if (buscarUsuario(usuario) != null) { // el user ya esta registrado
            return;
        }
        Usuario u = new Usuario(usuario, contra, personal);
        usuarios.add(u);
    }
    public void cerrarSesion() {
        usuarioActual = null;
    }
    private Usuario buscarUsuario(String nombre) {
        for (Usuario u : usuarios) {
            if (u.getUsuario().equals(nombre)) {
                return u;
            }
        }
        return null;
    }
    public boolean enviarMensaje(String receptor, String contenido) {
        Usuario recep = buscarUsuario(receptor);
        if (recep == null) {
            return false; // no existe el receptor
        }
        Mensaje nuevoMsj = new Mensaje(usuarioActual.getUsuario(), receptor, contenido);
        usuarioActual.enviarMensaje(nuevoMsj);
        recep.recibirMensaje(nuevoMsj);
        return true;
    }
    public boolean cerrarSistema() {
        if (!usuarioActual.getPersonal()) {
            return false;
        }
        sistemaAbierto = false;
        return true;
    }
    public void verMensajes() {
        usuarioActual.getMensajes();
    }
}
