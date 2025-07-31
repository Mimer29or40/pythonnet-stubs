namespace TestLib;

public class ExtractType
{
    public static void Basic(int param0) { }
    
    public static void Reference(ref int param0) { }
    
    public static void Generic<T>(T param0) { }
    
    public static void Nullable(int? param0) { }
    
    public static void UseGeneric(IEquatable<object> param0) { }
    
    public static void Array(int[] param0) { }

    public static class Nested { }
}