package Usuario;

import Mensaje.Mensaje;
import java.util.ArrayList;

public class Usuario {
    private String nombre;
    private String contrasena;
    private ArrayList<Mensaje> mensajesEnviados;
    private ArrayList<Mensaje> mensajesRecibidos;
    private boolean cargo;

    public Usuario(String nombre, String contrasena, boolean cargo) {
        this.nombre = nombre;
        this.contrasena = contrasena;
        this.mensajesEnviados = new ArrayList<Mensaje>();
        this.mensajesRecibidos = new ArrayList<Mensaje>();
        this.cargo = cargo;
    }

    public String getNombre() {
        return nombre;
    }
    public String getContrasena() {
        return contrasena;
    }
    public ArrayList<Mensaje> getMensajesEnviados() {
        return mensajesEnviados;
    }
    public ArrayList<Mensaje> getMensajesRecibidos() {
        return mensajesRecibidos;
    }
    public void recibirMensaje(Mensaje mensaje) {
        mensajesRecibidos.add(mensaje);
    }
    public boolean getCargo() {
        return cargo;
    }
    public void enviarMensaje(Mensaje mensaje) {
        mensajesEnviados.add(mensaje);
    }
}
