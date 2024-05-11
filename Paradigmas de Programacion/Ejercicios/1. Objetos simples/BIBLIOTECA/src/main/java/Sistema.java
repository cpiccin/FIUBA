import java.util.ArrayList;

public class Sistema {

    ArrayList<Libro> stock;
    ArrayList<Cliente> clientes;

    public Sistema() {
        this.stock = new ArrayList<Libro>();
        this.clientes = new ArrayList<Cliente>();
    }

    public void prestarLibro(Cliente cliente, String titulo) {
        if (!clientes.contains(cliente)) {
            clientes.add(cliente);
        }
        Libro libro = null;
        for (Libro l : stock) {
            if (l.getTitulo().equals(titulo)) {
                libro = l;
                break;
            }
        }
        cliente.prestar(libro);
        libro.prestado();
    }


    public int consultarStockTitulo(String titulo) {
        int cont = 0;
        for (Libro libro : stock) {
            if (libro.getTitulo().equals(titulo)) {
                cont += 1;
            }
        }
        return cont;
    }

    public int consultarStockFecha(String fecha) {
        // asumo fecha en formato DD-MM-AAAA
        int cont = 0;
        for (Libro libro : stock) {
            if (libro.getFecha().equals(fecha)) {
                cont += 1;
            }
        }
        return cont;
    }

    public int consultarStockAutor(String autores) {
        int cont = 0;
        for (Libro libro : stock) {
            if (libro.getAutor().equals(autores)) {
                cont += 1;
            }
        }
        return cont;
    }

    public void agregarLibro(String ISBN, String titulo, String fecha, String autores) {
        Libro nuevo = new Libro(ISBN, titulo, fecha, autores);
        stock.add(nuevo);
    }

    public void quitarLibro(Libro libro) {
        boolean remove = stock.remove(libro);
    }

    public void devolverLibro(Cliente cliente, Libro libro) {
        cliente.devolver(libro);
    }

    public void consultarLibrosPrestados(Cliente cliente) {
        for (Libro libro : cliente.getLibrosPrestados()) {
            System.out.println(libro.getTitulo() + " - " + libro.getAutor() + " - " + libro.getFecha() + "\n");
        }
    }

}
