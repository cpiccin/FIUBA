import java.util.ArrayList;

public class Alumno {
    String nombre;
    int padron;
    ArrayList<Carrera> carreras;
    ArrayList<Materia> materiasAprobadas;

    public Alumno(String nombre, int padron) {
        this.nombre = nombre;
        this.padron = padron;
        this.carreras = new ArrayList<Carrera>();
        this.materiasAprobadas = new ArrayList<Materia>();
    }

    public void inscribirCarrera(Carrera carrera) {
        this.carreras.add(carrera);
    }
    public void aprobarMateria(Materia materia) {
        this.materiasAprobadas.add(materia);
    }
    public ArrayList<Materia> getAprobadas() {
        return this.materiasAprobadas;
    }

}
