package ListaDeTareas.Logica;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import java.util.ArrayList;

public class Logica {
    private ArrayList<Tarea> tareas;

    public Logica() {
        tareas = new ArrayList<Tarea>();
    }

    public void agregarTarea(Tarea tarea) {
        tareas.add(tarea);
    }

    public ObservableList<Tarea> getTareas() {
        return FXCollections.observableArrayList(tareas);
    }

    public void eliminarTarea(Tarea tarea) {
        tareas.remove(tarea);
    }

}
