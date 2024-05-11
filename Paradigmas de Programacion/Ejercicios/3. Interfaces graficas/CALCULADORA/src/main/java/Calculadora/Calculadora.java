package Calculadora;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Calculadora extends Application {

    @Override
    public void start(Stage primaryStage) {
        Logica logica = new Logica();

        HBox hbox = new HBox();
        TextField n1 = new TextField();
        n1.setMaxWidth(70);
        TextField operacion = new TextField();
        operacion.setMaxWidth(30);
        TextField n2 = new TextField();
        n2.setMaxWidth(70);
        Button calcular = new Button("=");
        Label resultado = new Label();
        resultado.setFont(new Font(18));
        hbox.getChildren().addAll(n1, operacion, n2, calcular, resultado);

        calcular.setOnAction(event -> {
            int Intn1 = Integer.parseInt(n1.getText());
            int Intn2 = Integer.parseInt(n2.getText());
            String op = operacion.getText();
            int res = logica.calcular(Intn1, Intn2, op);
            resultado.setText(String.valueOf(res));
        });

        Scene scene = new Scene(hbox, 400, 25);

        primaryStage.setResizable(false);
        primaryStage.setTitle("Calculadora re boluda mal");
        primaryStage.setScene(scene);
        primaryStage.show();



    }


    public static void main(String[] args) {
        launch(args);
    }

}
