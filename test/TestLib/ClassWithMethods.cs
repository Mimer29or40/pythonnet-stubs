namespace TestLib
{
    public class ClassWithMethods
    {
        public int InstanceMethodWithDefaultParam(int param0 = 0) { return 0; }
        public int InstanceMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public int InstanceMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public int InstanceMethodWithNullableParam(int? param0) { return 0; }
        public int InstanceMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public int InstanceMethodWithParams0() { return 0; }
        public int InstanceMethodWithParams1(int param0) { return 0; }
        public int InstanceMethodWithParams2(int param0, int param1) { return 0; }
        public static int StaticMethodWithDefaultParam(int param0 = 0) { return 0; }
        public static int StaticMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableParam(int? param0) { return 0; }
        public static int StaticMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public static int StaticMethodWithParams0() { return 0; }
        public static int StaticMethodWithParams1(int param0) { return 0; }
        public static int StaticMethodWithParams2(int param0, int param1) { return 0; }
    }
}
