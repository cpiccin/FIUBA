public class main {

    public static void main(String[] args) {
        ColaSincronizada<Integer> cola = new ColaSincronizada<>(3);
        cola.encolar(1);
        cola.printCola();
        cola.encolar(2);
        cola.printCola();
        cola.encolar(3);
        cola.printCola();
        cola.encolar(4);
        cola.desencolar();
        cola.printCola();

        class Producer implements Runnable {
            private final BlockingQueue queue;

            Producer(BlockingQueue q) {
                queue = q;
            }
            public void run() {
                try {
                    while (true) {
                        queue.put(produce());
                    }
                } catch (InterruptedException ex) {
                }
            }
            Object produce() {
            };
        }

        class Consumer implements Runnable {
            private final BlockingQueue queue;
            Consumer(BlockingQueue q) {
                queue = q;
            }
            public void run() {
                try {
                    while (true) {
                        consume(queue. take());
                    }
                } catch (InterruptedException ex) {
                    }
            }

            void consume(Object x) {
                ...
            }
        }

        class Setup {
            void main() {
                BlockingQueue q = new SomeQueueImplementation();
                Producer p = new Producer(q);
                Consumer c1 = new Consumer(q);
                Consumer c2 = new Consumer(q);
                new Thread(p).start();
                new Thread(c1).start();
                new Thread(c2).start();
            } }
    }
}