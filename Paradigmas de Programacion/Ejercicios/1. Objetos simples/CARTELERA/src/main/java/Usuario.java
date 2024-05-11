import java.util.ArrayList;

public class Usuario {
    private String nombre;
    private String contra;
    private ArrayList<Mensaje> recibidos;
    private ArrayList<Mensaje> enviados;
    private boolean personal;

    public Usuario(String nombre, String contra, boolean esPersonal) {
        this.nombre = nombre;
        this.contra = contra;
        this.recibidos = new ArrayList<Mensaje>();
        this.enviados = new ArrayList<Mensaje>();
        this.personal = esPersonal;
    }
    public void enviarMensaje(Mensaje msj) {
        enviados.add(msj);
    }
    public void recibirMensaje(Mensaje msj) {
        recibidos.add(msj);
    }
    public void getMensajes() {
        System.out.println("Mensajes recibidos:");
        for (Mensaje m : recibidos) {
            System.out.println("De " + m.getReceptor() +": "+ m.getContenido());
        }
        System.out.println("Mensajes enviados:");
        for (Mensaje m : enviados) {
            System.out.println("Para "+ m.getEmisor() +": "+m.getContenido());
        }
    }
    public String getUsuario() {
        return this.nombre;
    }
    public boolean getPersonal() {
        return this.personal;
    }
    public String getContra() {
        return this.contra;
    }
    public ArrayList<Mensaje> getRecibidos() {
        return this.recibidos;
    }
    public ArrayList<Mensaje> getEnviados() {
        return this.enviados;
    }
}
