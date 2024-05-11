import javax.print.Doc;
import java.util.ArrayList;

public class Sistema {
    ArrayList<Usuario> usuarios;
    ArrayList<Docente> docentes;
    ArrayList<Alumno> alumnos;

    public Sistema(){
        usuarios = new ArrayList<Usuario>();
        docentes = new ArrayList<Docente>();
        alumnos = new ArrayList<Alumno>();
    }

    public boolean agregarUsuario(Usuario usuario) {
        if (usuario instanceof Docente) {
            Docente nuevo = (Docente) usuario;
            if (!docenteExiste(nuevo.getPadron())) {
                docentes.add(nuevo);
                return true;
            }
            return false;
        }
        if (usuario instanceof Alumno) {
            Alumno nuevo = (Alumno) usuario;
            if (!alumnoExiste(nuevo.getPadron())) {
                alumnos.add(nuevo);
                return true;
            }
            return false;
        }
        return false;
    }

    private boolean docenteExiste(String padron) {
        for (Docente docente : docentes) {
            if (docente.getPadron().equals(padron)) {
                return true;
            }
        }
        return false;
    }

    private boolean alumnoExiste(String padron) {
        for (Alumno alumno : alumnos) {
            if (alumno.getPadron().equals(padron)) {
                return true;
            }
        }
        return false;
    }

    public void listarDocentes() {
        System.out.println("---------Listado de docentes---------\n");
        for (Docente docente : docentes) {
            System.out.println("Nombre: " + docente.getNombre() + "\nPadron: "+ docente.getPadron() + "\nDNI: " + docente.getDNI() + "\n");
        }
    }

    public void listarAlumnos() {
        System.out.println("---------Listado de alumnos---------\n");
        for (Alumno alumno : alumnos) {
            System.out.println("Nombre: " + alumno.getNombre() + "\nPadron: "+ alumno.getPadron() + "\nDNI: " + alumno.getDNI() + "\n");
        }
    }
}
