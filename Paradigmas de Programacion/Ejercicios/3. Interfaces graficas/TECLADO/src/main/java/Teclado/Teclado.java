package Teclado;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;

public class Teclado extends Application {

    @Override

    public void start(Stage primaryStage) {
        VBox vbox = new VBox();
        Text msj = new Text("Presiona una tecla");
        msj.setFont(new Font(20));
        vbox.setAlignment(Pos.CENTER);
        vbox.getChildren().add(msj);
        Scene scene = new Scene(vbox, 300, 100);

        scene.setOnKeyPressed(event -> {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Tecla presionada");
            alert.setContentText(event.getCode().toString());
            alert.showAndWait();
        });

        primaryStage.setTitle("Que tecla presionaste?");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
