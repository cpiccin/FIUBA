public class Mensaje {
    private String contenido;
    private String emisor;
    private String receptor;

    public Mensaje(String emisor, String receptor, String contenido) {
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
