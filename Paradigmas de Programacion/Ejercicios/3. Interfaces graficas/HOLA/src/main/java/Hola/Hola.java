package Hola;


import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Hola extends Application {

    @Override
    public void start(Stage primaryStage) {

        VBox saludo = new VBox();
        Button boton = new Button("Saludar");
        TextField entrada = new TextField();
        entrada.setMaxWidth(100);
        saludo.getChildren().addAll(entrada, boton);
        saludo.setAlignment(Pos.CENTER);

        boton.setOnAction(e -> {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Saludo");
            alert.setHeaderText(null);
            alert.setContentText("Hola " + entrada.getText() + "!!!!!");
            alert.showAndWait();
        });

        VBox vbox = new VBox(saludo);
        Scene scene = new Scene(vbox, 200, 100);

        primaryStage.setResizable(false);
        primaryStage.setWidth(150);
        primaryStage.setHeight(100);
        primaryStage.setTitle("Hola");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
