namespace TestLib
{
    public struct StructWithInterface : IEquatable<StructWithInterface>
    {
        public override bool Equals(object? obj) { throw new NotImplementedException(); }
        public bool Equals(StructWithInterface? other) { throw new NotImplementedException(); }
        public bool Equals(StructWithInterface other) { throw new NotImplementedException(); }
        public override int GetHashCode() { throw new NotImplementedException(); }
        public static bool operator ==(StructWithInterface left, StructWithInterface right) => true;
        public static bool operator !=(StructWithInterface left, StructWithInterface right) => false;
    }

    public struct StructWithGeneric<T> { }

    public struct StructWithMultiGeneric<U, V> { }

    public struct StructWithFields
    {
        public const int InstanceFieldA = 0;
        public const int InstanceFieldB = 1;
        public const int InstanceFieldC = 2;

        public static readonly int StaticFieldA = 0;
        public static readonly int StaticFieldB = 1;
        public static readonly int StaticFieldC = 2;
    }

    public struct StructWithConstructors
    {
        public StructWithConstructors() { }
        public StructWithConstructors(int param0) { }
        public StructWithConstructors(int param0, int param1) { }
        public StructWithConstructors(int param0, int param1, int param2) { }
    }

    public struct StructWithProperties
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

    public struct StructWithMethods
    {
        public readonly int InstanceMethodWithDefaultParam(int param0 = 0) { return 0; }
        public readonly int InstanceMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public readonly int InstanceMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public readonly int InstanceMethodWithNullableParam(int? param0) { return 0; }
        public readonly int InstanceMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public readonly int InstanceMethodWithParams0() { return 0; }
        public readonly int InstanceMethodWithParams1(int param0) { return 0; }
        public readonly int InstanceMethodWithParams2(int param0, int param1) { return 0; }
        public static int StaticMethodWithDefaultParam(int param0 = 0) { return 0; }
        public static int StaticMethodWithNullableDefaultParam(int? param0 = 0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableOutParam(out int? param0) { param0 = 0; return 0; }
        public static int StaticMethodWithNullableParam(int? param0) { return 0; }
        public static int StaticMethodWithOutParam(out int param0) { param0 = 0; return 0; }
        public static int StaticMethodWithParams0() { return 0; }
        public static int StaticMethodWithParams1(int param0) { return 0; }
        public static int StaticMethodWithParams2(int param0, int param1) { return 0; }
    }
    public struct StructWithOperatorMethods
    {
        public override readonly bool Equals(object? obj) { return base.Equals(obj); }
        public override readonly int GetHashCode() { return base.GetHashCode(); }
        public static StructWithOperatorMethods operator +(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator -(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ++(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator --(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator +(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator -(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator *(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator /(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator %(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ~(StructWithOperatorMethods self) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator &(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator |(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator ^(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator <<(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static StructWithOperatorMethods operator >>>(StructWithOperatorMethods self, StructWithOperatorMethods other) => new StructWithOperatorMethods();
        public static bool operator !(StructWithOperatorMethods self) => true;
        public static bool operator true(StructWithOperatorMethods self) => true;
        public static bool operator false(StructWithOperatorMethods self) => false;
        public static bool operator ==(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator !=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator <(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator <=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator >(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
        public static bool operator >=(StructWithOperatorMethods self, StructWithOperatorMethods other) => true;
    }

    public readonly struct StructWithCollectionMethods : ICollection<int>
    {
        public int Count { get; }
        public bool IsReadOnly { get; }
        public void Add(int item) { }
        public void Clear() { }
        public bool Contains(int item) { return false; }
        public void CopyTo(int[] array, int arrayIndex) { }
        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() { throw new NotImplementedException(); }
        public IEnumerator<int> GetEnumerator() { throw new NotImplementedException(); }
        IEnumerator<int> IEnumerable<int>.GetEnumerator() { throw new NotImplementedException(); }
        public bool Remove(int item) { return false; }
    }

    public struct StructWithEvents
    {
        public event EventHandler? Event;
        public event EventHandler<EventArgs>? EventWitArgs;
    }

    public struct StructWithNested
    {
        public class NestedClass { }
        public struct NestedStruct { }
        public interface INestedInterface { }
        public enum NestedEnum { }
        public delegate void NestedDelegate();
    }
}
