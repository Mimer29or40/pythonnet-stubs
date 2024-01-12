namespace TestLib
{
    public interface IInterfaceWithSuper : IEquatable<IInterfaceWithSuper> { }

    public interface IInterfaceWithGeneric<T> { }

    public interface IInterfaceWithMultiGeneric<U, V> { }

    public interface IInterfaceWithFields
    {
        public const int InstanceFieldA = 0;
        public const int InstanceFieldB = 1;
        public const int InstanceFieldC = 2;

        public static readonly int StaticFieldA = 0;
        public static readonly int StaticFieldB = 1;
        public static readonly int StaticFieldC = 2;
    }

    public interface IInterfaceWithProperties
    {
        public int InstanceProperty0 { get; set; }
        public int InstanceProperty1 { get; set; }
        public int InstanceProperty2 { get; set; }
        public int InstanceReadOnlyProperty0 { get; }
        public int InstanceReadOnlyProperty1 { get; }
        public int InstanceReadOnlyProperty2 { get; }
        public static int StaticProperty0 { get; set; }
        public static int StaticProperty1 { get; set; }
        public static int StaticProperty2 { get; set; }
        public static int StaticReadOnlyProperty0 { get; }
        public static int StaticReadOnlyProperty1 { get; }
        public static int StaticReadOnlyProperty2 { get; }
    }

    public interface IInterfaceWithMethods
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

    public interface IInterfaceWithOperatorMethods
    {
        public static abstract IInterfaceWithOperatorMethods operator +(IInterfaceWithOperatorMethods self);
        public static abstract IInterfaceWithOperatorMethods operator -(IInterfaceWithOperatorMethods self);
        public static abstract IInterfaceWithOperatorMethods operator ++(IInterfaceWithOperatorMethods self);
        public static abstract IInterfaceWithOperatorMethods operator --(IInterfaceWithOperatorMethods self);
        public static abstract IInterfaceWithOperatorMethods operator +(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator -(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator *(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator /(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator %(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator ~(IInterfaceWithOperatorMethods self);
        public static abstract IInterfaceWithOperatorMethods operator &(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator |(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator ^(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator <<(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract IInterfaceWithOperatorMethods operator >>>(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract bool operator !(IInterfaceWithOperatorMethods self);
        public static abstract bool operator true(IInterfaceWithOperatorMethods self);
        public static abstract bool operator false(IInterfaceWithOperatorMethods self);
        //public static abstract bool operator ==(InterfaceWithOperatorMethods self, InterfaceWithOperatorMethods other);
        //public static abstract bool operator !=(InterfaceWithOperatorMethods self, InterfaceWithOperatorMethods other);
        public static abstract bool operator <(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract bool operator <=(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract bool operator >(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
        public static abstract bool operator >=(IInterfaceWithOperatorMethods self, IInterfaceWithOperatorMethods other);
    }

    public interface IInterfaceWithCollectionMethods : ICollection<int> { }

    public interface IInterfaceWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWitArgs;
    }

    public interface IInterfaceWithNested
    {
        public class NestedClass { }
        public struct NestedStruct { }
        public interface INestedInterface { }
        public enum NestedEnum { }
        public delegate void NestedDelegate();
    }
}
