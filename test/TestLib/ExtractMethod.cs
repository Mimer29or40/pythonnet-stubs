namespace TestLib;

public class ExtractMethod<T>
{
    public void Basic() { }

    public void Parameters(int param0, int param1) { }

    public int Out(out int param) { param = 0; return 0; }

    public void VoidOut(out int param) { param = 0; }

    public static void Static() { }
    
    public void GenericClass(T param) { }
    
    public void GenericMethod<T0, T1>(T0 param0, T1 param1) { }
    
    public void GenericBoth<T0, T1>(T param, T0 param0, T1 param1) { }

    public void GenericOut<TOut>(out TOut param) { param = default(TOut) ?? throw new InvalidOperationException(); }

    public void GenericConstraint<TP>(TP param) where TP: IConvertible {  }
}