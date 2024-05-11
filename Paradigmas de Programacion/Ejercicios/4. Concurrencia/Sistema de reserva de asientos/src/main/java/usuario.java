
public class usuario implements Runnable {
    private cine cine;
    private int asientoElegido;

    public usuario(cine cine, int asientoElegido) {
        this.cine = cine;
        this.asientoElegido = asientoElegido;
    }

    @Override
    public void run() {
       cine.reservar(asientoElegido);
    }

}
