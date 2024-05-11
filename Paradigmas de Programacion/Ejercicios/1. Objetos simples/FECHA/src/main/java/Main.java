public class Main {
    public static void main(String[] args) {
        Fecha fecha1 = new Fecha(1, 1, 2020);
        System.out.println(fecha1);
        Fecha fecha2 = new Fecha("Enero", 1, 2020);
        System.out.println(fecha2);
        Fecha fecha3 = new Fecha(1, 2020);
        System.out.println(fecha3);
    }
}
