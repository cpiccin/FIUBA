import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Fiuba sistema = new Fiuba();
        Materia algebra = new Materia("Algebra", 9012, 8);
        Materia analisis = new Materia("Analisis", 9013, 8);
        Materia fisica = new Materia("Fisica", 7014, 8);
        Materia quimica = new Materia("Quimica", 8015, 6);
        Materia ingles = new Materia("Ingles", 1016, 4);
        Materia taller = new Materia("Taller", 1017, 6);
        Materia algo1 = new Materia("Algoritmos 1", 7518, 6);
        Materia algo2 = new Materia("Algoritmos 2", 7519, 6);
        Materia algo3 = new Materia("Algoritmos 3", 7520, 6);
        Materia legal = new Materia("Aspectos Legales", 10121, 4);
        Materia economia = new Materia("Economia", 10122, 4);
        Materia sistemas = new Materia("Sistemas Operativos", 7523, 6);
        Materia redes = new Materia("Redes", 7524, 6);
        Materia bd = new Materia("Bases de Datos", 7525, 6);
        Materia probabilidad = new Materia("Probabilidad y Estadistica", 90126, 6);
        Materia arqui = new Materia("Arquitectura de Computadoras", 7527, 6);
        List<Materia> obligatoriasElectro = new ArrayList<Materia>();
        obligatoriasElectro.add(algebra);
        obligatoriasElectro.add(analisis);
        obligatoriasElectro.add(fisica);
        obligatoriasElectro.add(ingles);
        obligatoriasElectro.add(algo1);
        obligatoriasElectro.add(legal);
        obligatoriasElectro.add(economia);
        List<Materia> obligatoriasInf = new ArrayList<Materia>();
        obligatoriasInf.add(algebra);
        obligatoriasInf.add(analisis);
        obligatoriasInf.add(fisica);
        obligatoriasInf.add(ingles);
        obligatoriasInf.add(algo2);
        obligatoriasInf.add(algo1);
        obligatoriasInf.add(algo3);
        obligatoriasInf.add(legal);
        obligatoriasInf.add(sistemas);
        obligatoriasInf.add(redes);
        obligatoriasInf.add(bd);
        obligatoriasInf.add(probabilidad);
        obligatoriasInf.add(arqui);
        List<Materia> optativasElectro = new ArrayList<Materia>();
        optativasElectro.add(algo2);
        optativasElectro.add(algo3);
        optativasElectro.add(sistemas);
        optativasElectro.add(redes);
        List<Materia> optativasInf = new ArrayList<Materia>();
        optativasInf.add(legal);
        optativasInf.add(economia);
        optativasInf.add(taller);

        Carrera electronica = new Carrera("Ingenieria en Electronica", obligatoriasElectro, optativasElectro, 203);
        Carrera informatica = new Carrera("Ingenieria en Informatica", obligatoriasInf, obligatoriasInf,192);
        Alumno candela = new Alumno("Candela Piccin", 109760);

        sistema.inscribir(candela, informatica);
        sistema.inscribir(candela, electronica);
        sistema.aprobar(candela, algebra);
        sistema.aprobar(candela, analisis);
        sistema.aprobar(candela, fisica);
        sistema.aprobar(candela, ingles);
        sistema.aprobar(candela, algo1);
        sistema.aprobar(candela, legal);
        sistema.aprobar(candela, economia);
        sistema.getEstado(candela);

    }
}