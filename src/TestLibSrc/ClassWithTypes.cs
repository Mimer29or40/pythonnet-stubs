namespace TestLib
{
    public static class ClassWithTypes
    {
        public static void MethodReturnsVoid() { }
        public static byte MethodReturnsByte() { return 0; }
        public static sbyte MethodReturnsSByte() { return 0; }
        public static short MethodReturnsInt16() { return 0; }
        public static ushort MethodReturnsUInt16() { return 0; }
        public static int MethodReturnsInt32() { return 0; }
        public static uint MethodReturnsUInt32() { return 0; }
        public static long MethodReturnsInt64() { return 0; }
        public static ulong MethodReturnsUInt64() { return 0; }
        public static float MethodReturnsSingle() { return 0; }
        public static double MethodReturnsDouble() { return 0; }
        public static bool MethodReturnsBoolean() { return false; }
        public static char MethodReturnsChar() { return (char) 0; }
        public static string MethodReturnsString() { return ""; }
        public static object MethodReturnsObject() { return new Object(); }
    }
}
