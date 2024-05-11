import java.util.ArrayList;

public class ListaDuplicanteComp<T> {
    private final ArrayList<T> elementos;

    public ListaDuplicanteComp() {
        elementos = new ArrayList<>();
    }

    public void add(T elem) {
        elementos.add(elem);
        elementos.add(elem);
    }

    public T get(int i) {
        return elementos.get(i);
    }

}
