import java.util.ArrayList;

public class Cliente {
    String nombre;
    ArrayList<Libro> librosPrestados;

    public Cliente(String nombre) {
        this.nombre = nombre;
        this.librosPrestados = new ArrayList<Libro>();
    }

    public String getNombre() {
        return nombre;
    }

    public ArrayList<Libro> getLibrosPrestados() {
        return librosPrestados;
    }

    public void prestar(Libro libro) {
        librosPrestados.add(libro);
    }

    public void devolver(Libro libro) {
        librosPrestados.remove(libro);
    }
}
