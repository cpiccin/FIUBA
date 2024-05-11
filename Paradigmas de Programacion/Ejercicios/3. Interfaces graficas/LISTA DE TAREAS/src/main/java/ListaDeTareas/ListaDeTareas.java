package ListaDeTareas;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import ListaDeTareas.Logica.Logica;
import ListaDeTareas.Logica.Tarea;

public class ListaDeTareas extends Application {

    private Logica logica;

    @Override
    public void start(Stage primaryStage) {
        logica = new Logica();

        TextField nuevaTarea = new TextField();
        Button botonAgregar = new Button("Agregar tarea");
        ListView<Tarea> listaTareas = new ListView<>();

        botonAgregar.setOnAction(event -> {
            logica.agregarTarea(new Tarea(nuevaTarea.getText()));
            nuevaTarea.clear();
            listaTareas.setItems(logica.getTareas());
        });

        listaTareas.setCellFactory(param -> new ListCell<>() { // Setting a cell factory for the ListView named listaTareas. The cell factory is a function that tells the ListView how to create and display each cell.
            @Override
            protected void updateItem(Tarea tarea, boolean empty) {
                super.updateItem(tarea, empty);
                if (empty || tarea == null) {
                    setText(null);
                    setGraphic(null);
                } else {
                    setText(tarea.getContenido());

                    ToggleButton toggleButton = new ToggleButton("Done");
                    toggleButton.setSelected(tarea.isCompletada()); // se marca si la tarea esta completada
                    toggleButton.setOnAction(event -> tarea.completar()); // si no, se completa

                    Button deleteButton = new Button("Delete");
                    deleteButton.setOnAction(event -> {
                        getListView().getItems().remove(getItem());
                        logica.eliminarTarea(tarea);
                    });

                    HBox hBox = new HBox(toggleButton, deleteButton);
                    hBox.setSpacing(10);

                    setGraphic(hBox);
                }
            }
        });

        VBox vbox = new VBox();
        vbox.getChildren().addAll(nuevaTarea, botonAgregar, listaTareas);
        Scene scene = new Scene(vbox, 400, 600);

        primaryStage.setTitle("TODO List");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}