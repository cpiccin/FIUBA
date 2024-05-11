package ChoiceBoxEj;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class ChoiceBoxEj extends Application {

    @Override
    public void start(Stage primaryStage) {
        ChoiceBox<String>  choiceBox = new ChoiceBox<>();
        choiceBox.getItems().addAll("Red", "Blue", "Pink", "Green", "Yellow", "Black", "White");
        choiceBox.setValue("Red");
        Label label = new Label("I'm a color");
        label.setFont(new Font(20));

        // agrego listener
        choiceBox.getSelectionModel().selectedItemProperty().addListener((v, oldValue, newValue) -> {
            label.setTextFill(Color.valueOf(newValue));
        });


        VBox vbox = new VBox();
        vbox.getChildren().addAll(choiceBox, label);

        Scene scene = new Scene(vbox, 150, 50);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}
