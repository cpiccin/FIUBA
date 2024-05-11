public class Main {
    public static void main(String[] args) {
        Sistema biblioteca = new Sistema();
        biblioteca.agregarLibro("978-84-376-0494-7", "El Quijote", "01-01-1605", "Miguel de Cervantes");
        biblioteca.agregarLibro("948-12-124-9842-0", "Martin Fierro", "02-01-1872", "Jose Hernandez");
        biblioteca.agregarLibro("535-32-673-0101-9", "El Aleph", "01-01-1949", "Jorge Luis Borges");
        biblioteca.agregarLibro("123-45-678-9012-3", "", "01-01-2021", "Autor Anonimo");
        biblioteca.agregarLibro("546-78-211-3123-0", "El Matadero", "01-01-1871", "Esteban Echeverria");
        biblioteca.agregarLibro("978-84-376-0494-7", "Ficciones", "01-01-1944", "Jorge Luis Borges");
        Cliente cliente1 = new Cliente("Juan");
        Cliente cliente2 = new Cliente("Pedro");
        Cliente cliente3 = new Cliente("Maria");
        int stock1 = biblioteca.consultarStockAutor("Jorge Luis Borges");
        System.out.println("Stock de libros de Jorge Luis Borges: " + stock1);
        int stock2 = biblioteca.consultarStockTitulo("El Quijote");
        System.out.println("Stock de El Quijote: " + stock2);
        biblioteca.prestarLibro(cliente2, "El Quijote");
        biblioteca.consultarLibrosPrestados(cliente2);
        int stock3 = biblioteca.consultarStockTitulo("El Quijote");
        System.out.println("Stock de El Quijote: " + stock3);
    }
}
