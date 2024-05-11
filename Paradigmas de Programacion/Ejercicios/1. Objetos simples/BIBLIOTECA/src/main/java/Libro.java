import java.util.ArrayList;

public class Libro {
    private final String ISBN;
    private final String titulo;
    private final String autores;
    private final String fecha;
    private boolean prestado;

    public Libro(String ISBN, String titulo, String fecha,  String autores) {
        this.ISBN = ISBN;
        this.titulo = titulo;
        this.autores = autores;
        this.fecha = fecha;
        this.prestado = false;
    }

    public void prestado() {
        prestado = true;
    }
    public void devuelto() {
        prestado = false;
    }

    public boolean getPrestado() {
        return prestado;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return String.join(", ", autores);
    }
    public String getFecha() {
        return fecha;
    }

}
