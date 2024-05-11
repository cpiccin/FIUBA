package ListaDeTareas.Logica;

public class Tarea {
    String contenido;
    boolean completada;

    public Tarea(String contenido) {
        this.contenido = contenido;
        this.completada = false;
    }

    public String getContenido() {
        return contenido;
    }

    public boolean isCompletada() {
        return completada;
    }

    public void completar() {
        completada = true;
    }
}
