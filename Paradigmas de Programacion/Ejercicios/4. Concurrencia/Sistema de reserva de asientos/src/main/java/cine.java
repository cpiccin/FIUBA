public class cine {
    private boolean[] asientos;

    public cine(int numDeAsientos) {
        asientos = new boolean[numDeAsientos];
    }

    public synchronized boolean reservar(int asiento) {
        if (!asientos[asiento]) {
            // el asiento no esta ocupado
            asientos[asiento] = true; // reservo el asiento
            System.out.println("Asiento "+asiento+ " reservado");
            return true;
        }
        System.out.println("Asiento " + asiento + " ocupado");
        return false;
    }
}
