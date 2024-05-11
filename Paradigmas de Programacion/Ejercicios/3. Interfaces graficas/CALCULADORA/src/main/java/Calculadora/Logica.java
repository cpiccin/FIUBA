package Calculadora;

public class Logica {

    public int calcular(int a, int b, String operacion) {
        if (operacion.equals("+")) {
            return sumar(a, b);
        } else if (operacion.equals("-")) {
            return restar(a, b);
        } else if (operacion.equals("*")) {
            return multiplicar(a, b);
        } else if (operacion.equals("/")) {
            return dividir(a, b);
        }
        return 0;
    }

    private int sumar(int a, int b){
        return a + b;
    }

    private int restar(int a, int b){
        return a - b;
    }

    private int multiplicar(int a, int b){
        return a * b;
    }

    private int dividir(int a, int b) {
        return a / b;
    }

}
