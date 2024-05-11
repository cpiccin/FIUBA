public class Main {
    private static int variable = 0;
    private static final Object lock = new Object();

    public static class Hilo1 extends Thread {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    System.out.println("La variable es: " + variable);
                    variable++;
                }
            }
        }
    }
    public static class Hilo2 implements Runnable {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    System.out.println("La variable es: " + variable);
                    variable++;
                }
            }
        }
    }

    public static void main(String[] args) {
        Hilo1 h1 = new Hilo1();
        Hilo2 h2 = new Hilo2();
        Thread th2 = new Thread(h2);
        h1.start();
        th2.start();
    }
}

