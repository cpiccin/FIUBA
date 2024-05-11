import java.util.ArrayList;
import java.util.List;

public class Fiuba {
    Fiuba sistema;
    List<Alumno> alumnos;
    List<Carrera> carreras;

    public Fiuba() {
        this.alumnos = new ArrayList<Alumno>();
        this.carreras = new ArrayList<Carrera>();
    }
    public void getEstado(Alumno alumno) {
        int cont = 0;
        System.out.println("Alumno: " + alumno.nombre);
        System.out.println("Padron: " + alumno.padron);
        System.out.println("Carreras inscriptas: ");
        for (Carrera carrera : alumno.carreras) {
            System.out.println(carrera.getNombre());
            System.out.println("    Materias aprobadas: ");
            for (Materia materia : carrera.getObligatorias()) {
                if (alumno.getAprobadas().contains(materia)) {
                    System.out.println("        " + materia.getNombre() + " " + materia.getCodigo());
                    cont += materia.getCreditos();
                }
            }
            System.out.println("Creditos acumulados: " + cont);
            cont = 0;
        }
    }
    public void inscribir(Alumno alumno, Carrera carrera) {
        alumno.inscribirCarrera(carrera);
    }
    public void aprobar(Alumno alumno, Materia materia) {
        alumno.aprobarMateria(materia);
    }

    public void addAlumno(Alumno alumno) {
        this.alumnos.add(alumno);
    }

    public void addCarrera(Carrera carrera) {
        this.carreras.add(carrera);
    }
}
