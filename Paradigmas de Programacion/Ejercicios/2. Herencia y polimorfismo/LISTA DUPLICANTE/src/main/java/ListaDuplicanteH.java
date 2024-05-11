import java.util.ArrayList;

public class ListaDuplicanteH<T>  extends ArrayList<T>{
    // no es necesario @Override para get() porque no cambia el comportamiento para esta implementacion

    @Override
    public boolean add(T elem) {
        super.add(elem);
        super.add(elem);
        return true;
    }
}
