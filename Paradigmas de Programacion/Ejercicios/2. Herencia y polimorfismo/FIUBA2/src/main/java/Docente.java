public class Docente extends Usuario{
    private String padron;

    public Docente(String nombre, String DNI, String padron) {
        super(nombre, DNI);
        this.padron = padron;
    }

    public String getPadron() {
        return padron;
    }
}
