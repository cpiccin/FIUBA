public class Fecha {
    int mes;
    int dia;
    int anio;

    public Fecha(int mes, int dia, int anio) {
        this.mes = mes;
        this.dia = dia;
        this.anio = anio;
    }

    public Fecha(String mes, int dia, int anio) {
        this.mes = mesAInt(mes);
        this.dia = dia;
        this.anio = anio;
    }

    public Fecha(int dias, int anio) {
        this.mes = encontrarMes(dias);
        this.dia = encontrarDia(dias, this.mes);
        this.anio = anio;
    }

    private int mesAInt(String mes) {
        String[] meses = {"", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
        "Octubre", "Noviembre", "Diciembre"};
        for (int i = 0; i <= 12; i++) {
            if (mes.equals(meses[i])) {
                return i;
            }
        }
        return 0;
    }

    private int encontrarMes(int dias) {
        int mes = 0;
        int[] diasPorMes = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        for (int i = 1; i <= 12; i++) {
            if (dias <= diasPorMes[i]) {
                mes = i;
                break;
            }
        }
        return this.mes = mes;
    }
    private int encontrarDia(int dias, int mes) {
        int[] diasPorMes = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        int dia = dias - diasPorMes[mes - 1];
        return dia;
    }

    @Override
    public String toString() {
        return this.mes + "/" + this.dia + "/" + this.anio;
    }

}
