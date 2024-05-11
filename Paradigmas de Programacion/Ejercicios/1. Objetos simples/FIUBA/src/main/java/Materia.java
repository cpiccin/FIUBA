public class Materia {
    String nombre;
    int codigo;
    int creditos;

    public Materia(String nombre, int codigo, int creditos) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.creditos = creditos;
    }
    public String getNombre() {
        return this.nombre;
    }
    public int getCodigo() {
        return this.codigo;
    }
    public int getCreditos() {
        return this.creditos;
    }
}
