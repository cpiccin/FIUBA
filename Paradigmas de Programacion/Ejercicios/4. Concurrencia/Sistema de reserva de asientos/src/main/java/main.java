import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class main {

    public static void main(String[] args) {
        cine cine = new cine(2);
        Random rand = new Random();
        List<usuario> reservas = new ArrayList<>();

        for (int i = 0; i < 4; i++) {
            reservas.add(new usuario(cine, rand.nextInt(2)));
        }

        for (int i = 0; i < 4; i++) {
            new Thread(reservas.get(i), "user"+i).start();
        }

    }



}
