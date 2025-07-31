namespace TestLib;

public class ExtractParameter
{
    public static void Basic(int param) { }

    public static void Default(int param = 0) { }

    public static void Out(out int param) { param = 0; }
}