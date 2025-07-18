namespace TestLib
{
    public interface IInterfaceWithMethods
    {
        public abstract int InstanceMethodWithDefaultParam(int param0 = 0);
        public abstract int InstanceMethodWithNullableDefaultParam(int? param0 = 0);
        public abstract int InstanceMethodWithNullableOutParam(out int? param0);
        public abstract int InstanceMethodWithNullableParam(int? param0);
        public abstract int InstanceMethodWithOutParam(out int param0);
        public abstract int InstanceMethodWithParams();
        public abstract int InstanceMethodWithParams(int param0);
        public abstract int InstanceMethodWithParams(int param0, int param1);
        //public abstract static int StaticMethodWithDefaultParam(int param0 = 0);
        //public abstract static int StaticMethodWithNullableDefaultParam(int? param0 = 0);
        //public abstract static int StaticMethodWithNullableOutParam(out int? param0);
        //public abstract static int StaticMethodWithNullableParam(int? param0);
        //public abstract static int StaticMethodWithOutParam(out int param0);
        //public abstract static int StaticMethodWithParams();
        //public abstract static int StaticMethodWithParams(int param0);
        //public abstract static int StaticMethodWithParams(int param0, int param1);
    }
}
