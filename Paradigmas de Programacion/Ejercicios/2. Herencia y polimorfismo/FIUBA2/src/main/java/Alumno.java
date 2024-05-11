public class Alumno extends Usuario{
    private String padron;

    public Alumno(String nombre, String DNI, String padron) {
        super(nombre, DNI);
        this.padron = padron;
    }

    public String getPadron() {
        return padron;
    }
}
