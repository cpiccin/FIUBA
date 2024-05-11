package Mensaje;

public class Mensaje {
    String contenido;
    String emisor;
    String receptor;

    public Mensaje(String contenido, String emisor, String receptor) {
        this.contenido = contenido;
        this.emisor = emisor;
        this.receptor = receptor;
    }
    public String getContenido() {
        return contenido;
    }
    public String getEmisor() {
        return emisor;
    }
    public String getReceptor() {
        return receptor;
    }

}
