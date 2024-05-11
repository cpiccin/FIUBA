package Coordenadas;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class Coordenadas extends Application {

    @Override
    public void start(Stage primaryStage) {
        Label coordenadas = new Label("X: 0.0 , Y: 0.0");
        coordenadas.setFont(new Font(20));
        VBox vbox = new VBox();
        vbox.setAlignment(Pos.CENTER);
        vbox.getChildren().add(coordenadas);
        Scene scene = new Scene(vbox, 400, 400);

        scene.setOnMouseMoved(event -> {
           double X = event.getX();
           double Y = event.getY();
           coordenadas.setText("(X: " + X + " , " + "Y: " + Y + ")");
        });

        primaryStage.setTitle("Coordenadas de tu mouse");
        primaryStage.setScene(scene);
        primaryStage.show();

    }



    public static void main(String[] args) {
        launch(args);
    }

}
