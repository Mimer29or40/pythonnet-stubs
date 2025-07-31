namespace TestLib;

public class ExtractMethod
{
    public void Basic() { }

    public void Parameters(int param0, int param1) { }

    public int Out(out int param) { param = 0; return 0; }

    public void VoidOut(out int param) { param = 0; }

    public static void Static() { }
}