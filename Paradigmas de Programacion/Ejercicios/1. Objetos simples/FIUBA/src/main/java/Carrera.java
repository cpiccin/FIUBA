import java.util.List;

public class Carrera {
    String nombre;
    List<Materia> materiasObligatorias;
    List<Materia> materiasOptativas;
    int creditosMinimos;

    public Carrera(String nombre, List<Materia> materiasObligatorias, List<Materia> materiasOptativas, int creditosMinimos) {
        this.nombre = nombre;
        this.materiasObligatorias = materiasObligatorias;
        this.materiasOptativas = materiasOptativas;
        this.creditosMinimos = creditosMinimos;
    }
    public String getNombre() {
        return this.nombre;
    }
    public int getCreditosMinimos() {
        return this.creditosMinimos;
    }
    public List<Materia> getObligatorias() {
        return this.materiasObligatorias;
    }
    public List<Materia> getOptativas() {
        return this.materiasOptativas;
    }
}
